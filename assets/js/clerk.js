
// Central protection map (paths not listed are PUBLIC)
const pageAccessConfig = {
  // --- Admin (your current mix kept) ---
  '/assets/admin/kidscodingcourse/scratch.html': {},                 
  '/assets/admin/kidscodingcourse/scratchdemo.html': { role: 'admin' },
  '/assets/admin/kidscodingcourse/python.html': {},                  
  '/assets/admin/kidscodingcourse/pythondemo.html': { role: 'admin' },
  '/assets/admin/kidscodingcourse/webbeginner.html': {},             
  '/assets/admin/kidscodingcourse/webbeginnerdemo.html': { role: 'admin' },

  // --- Kids coding (role: coding) ---
  '/assets/scratch/scratch.html': { role: 'coding' },
  '/assets/python/python.html': { role: 'coding' },
  '/assets/java/java.html': { role: 'coding' },
  '/assets/webdevkids/beginner.html': { role: 'coding' },
  '/assets/webdevkids/advanced.html': { role: 'coding' },

  // --- Robotics ---
  '/assets/robotics/level1/level1.html': { role: 'robotics' },

  // --- AI ---
  '/assets/ai/level1.html': { role: 'ai' },
  '/assets/ai/level2.html': { role: 'ai' },

  // --- College ---
  '/assets/college/college.html': { role: 'college' }
};

// --- Helpers ---
function getUserRolesAndPerms(user) {
  const md = user?.publicMetadata || {};
  const roles = Array.isArray(md.roles) ? md.roles.filter(Boolean) : (md.role ? [md.role] : []);
  const perms = Array.isArray(md.permissions) ? md.permissions : [];
  return { roles, perms };
}

// Ensure leading slash for reliable lookups
function normalizePath(path) {
  if (!path) return '/';
  return path.startsWith('/') ? path : '/' + path;
}

function getAccessRequirementForUrl(href) {
  const url = new URL(href, window.location.href);
  const path = normalizePath(url.pathname);

  // direct match
  if (pageAccessConfig[path]) return pageAccessConfig[path];

  // fallback: try without trailing slashes (if any)
  const trimmed = path.replace(/\/+$/, '') || '/';
  if (pageAccessConfig[trimmed]) return pageAccessConfig[trimmed];

  // default public
  return {};
}

function hasAccess(user, requirement) {
  if (!requirement || Object.keys(requirement).length === 0) return true; // public
  if (requirement.auth && !user) return false;
  if (!user && (requirement.role || requirement.permission)) return false;

  if (user) {
    const { roles, perms } = getUserRolesAndPerms(user);
    if (requirement.role && !roles.includes(requirement.role)) return false;
    if (requirement.permission && !perms.includes(requirement.permission)) return false;
  }
  return true;
}

function showSignInRequired() {
  const m = new bootstrap.Modal(document.getElementById('signinRequiredModal'));
  m.show();
}

function showAccessDenied() {
  const m = new bootstrap.Modal(document.getElementById('accessDeniedModal'));
  m.show();
}

// Guard direct-URL visits
function guardCurrentPageOnLoad(user) {
  const path = normalizePath(window.location.pathname);
  const req = pageAccessConfig[path];
  if (!req) return; // public page

  if (!hasAccess(user, req)) {
    if (!user) {
      window.location.href = 'index.html';
    } else {
      document.body.innerHTML = `
        <div class="container py-5">
          <div class="text-center">
            <div class="mb-3" style="font-size:56px;color:#dc3545;"><i class="fas fa-ban"></i></div>
            <h2>Access Denied</h2>
            <p class="text-muted">You don't have permission to access this page.</p>
            <a href="/" class="btn btn-primary mt-2"><i class="fas fa-arrow-left me-2"></i>Return to Dashboard</a>
          </div>
        </div>
      `;
    }
  }
}

async function initAccess() {
  // Wait (up to 10s) for Clerk to be present; site still works as public if not
  if (typeof window.Clerk === 'undefined') {
    await new Promise((resolve) => {
      const t = setInterval(() => {
        if (typeof window.Clerk !== 'undefined') { clearInterval(t); resolve(); }
      }, 100);
      setTimeout(() => resolve(), 10000);
    });
  }

  try {
    if (window.Clerk) {
      await window.Clerk.load({ debug: true });

      // Modal buttons → Clerk UIs
      document.getElementById('signin-required-btn')?.addEventListener('click', () => {
        const el = document.getElementById('signinRequiredModal');
        (bootstrap.Modal.getInstance(el) || new bootstrap.Modal(el)).hide();
        window.Clerk.openSignIn();
      });
      document.getElementById('signup-required-btn')?.addEventListener('click', () => {
        const el = document.getElementById('signinRequiredModal');
        (bootstrap.Modal.getInstance(el) || new bootstrap.Modal(el)).hide();
        window.Clerk.openSignUp();
      });
    }
  } catch (e) {
    console.warn('Clerk load error:', e);
  }

  // Intercept ALL internal link clicks (keeps your card HTML untouched)
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href]');
    if (!a) return;

    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return;

    const url = new URL(href, window.location.href);
    if (url.origin !== window.location.origin) return; // external link

    const req = getAccessRequirementForUrl(href);
    const user = window.Clerk?.user || null;

    if (!hasAccess(user, req)) {
      e.preventDefault();
      if (!user && (req.auth || req.role || req.permission)) {
        showSignInRequired();
      } else {
        showAccessDenied();
      }
    }
  });

  // Protect direct page loads
  guardCurrentPageOnLoad(window.Clerk?.user || null);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initAccess);
} else {
  initAccess();
}
