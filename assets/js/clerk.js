// DOM elements
const signInBtn = document.getElementById('sign-in-btn');
const signUpBtn = document.getElementById('sign-up-btn');
const signOutBtn = document.getElementById('sign-out-btn');
const statusMessage = document.getElementById('status-message');
const authButtons = document.getElementById('auth-buttons');
const userInfo = document.getElementById('user-info');
const userAvatar = document.getElementById('user-avatar');
const userName = document.getElementById('user-name');
const signInLoader = document.getElementById('sign-in-loader');
const signUpLoader = document.getElementById('sign-up-loader');
const adminPanel = document.getElementById('admin-panel');

// Page access configuration based on user metadata
const pageAccessConfig = {
  'assets/scratch/scratch.html': { role: 'coding' },
  'assets/python/python.html': { role: 'coding' },
  'assets/java/java.html': { role: 'coding' },
  'assets/webdevkids/beginner.html': { role: 'coding' },
  'assets/webdevkids/advanced.html': { role: 'coding' },

  'assets/robotics/level1/level1.html': { role: 'robotics' },

  'assets/ai/level1.html': { role: 'ai' },
  'assets/ai/level2.html': { role: 'ai' },

  'assets/admin/kidscodingcourse/python.html': { role: 'admin' },
  'assets/admin/kidscodingcourse/scratch.html': { role: 'admin' },
  'assets/admin/kidscodingcourse/webbeginner.html': { role: 'admin' },

  'assets/college/college.html': { role: 'college' }
};

// Show status message
function showMessage(message, type) {
  statusMessage.textContent = message;
  statusMessage.className = `status-message alert alert-${type} animate__animated animate__fadeIn`;
  statusMessage.style.display = "block";
  setTimeout(() => {
    statusMessage.className = `status-message alert alert-${type} animate__animated animate__fadeOut`;
    setTimeout(() => { statusMessage.style.display = "none"; }, 500);
  }, 4500);
}

// Check if user has access to a specific page based on metadata
function hasPageAccess(user, page) {
  if (!pageAccessConfig[page]) return true; // Public page

  const config = pageAccessConfig[page];
  const userMetadata = user.publicMetadata || {};

  // Role-based access (supports "role" or "roles" array)
  if (config.role) {
    const userRoles = Array.isArray(userMetadata.roles)
      ? userMetadata.roles
      : [userMetadata.role]; // fallback for single role

    if (!userRoles.includes(config.role)) {
      return false;
    }
  }

  // Permission-based access
  if (config.permission) {
    if (!userMetadata.permissions || !userMetadata.permissions.includes(config.permission)) {
      return false;
    }
  }

  return true;
}

// Handle authentication
function handleUserAuthentication(user) {
  const email = user.primaryEmailAddress?.emailAddress || 'User';
  const name = user.firstName || email;

  userName.textContent = 'Welcome, ' + name + '!';

  if (window.Clerk.user.imageUrl) {
    userAvatar.src = window.Clerk.user.imageUrl;
  } else if (window.Clerk.user.profileImageUrl) {
    userAvatar.src = window.Clerk.user.profileImageUrl;
  } else {
    userAvatar.src = 'https://www.gravatar.com/avatar/?d=mp';
  }

  authButtons.style.display = "none";
  userInfo.style.display = "block";

  // Admin access only if user has admin role
  const userMetadata = user.publicMetadata || {};
  const userRoles = Array.isArray(userMetadata.roles)
    ? userMetadata.roles
    : [userMetadata.role];

  if (userRoles.includes('admin')) {
    adminPanel.style.display = 'block';
    showMessage("Welcome back, Admin! You have full access.", "success");
  } else {
    adminPanel.style.display = 'none';
    showMessage("You have limited access.", "warning");
  }

  sessionStorage.setItem('isAuthenticated', 'true');
  sessionStorage.setItem('userEmail', email);

  // Page access check for protected pages
  const currentPage = window.location.pathname.replace(/^.*[\\/]/, '');
  if (!hasPageAccess(user, currentPage)) {
    showAccessDenied();
  }
}

// Show access denied page
function showAccessDenied() {
  document.body.innerHTML = `
    <div class="access-denied-container">
      <div class="access-denied">
        <div class="access-denied-icon">
          <i class="fas fa-ban"></i>
        </div>
        <h2>Access Denied</h2>
        <p>You don't have permission to access this page. Please contact the administrator if you believe this is an error.</p>
        <a href="index.html" class="access-denied-btn">
          <i class="fas fa-arrow-left me-2"></i>Return to Dashboard
        </a>
      </div>
    </div>
  `;
}

// Sign out
function handleUserSignOut() {
  showMessage("Signed out successfully.", "success");
  authButtons.style.display = "block";
  userInfo.style.display = "none";
  adminPanel.style.display = "none";
  sessionStorage.clear();
}

// Initialize Clerk
async function loadClerk() {
  try {
    signInLoader.style.display = 'inline-block';
    signUpLoader.style.display = 'inline-block';
    signInBtn.disabled = true;
    signUpBtn.disabled = true;

    if (typeof window.Clerk === 'undefined') {
      await new Promise((resolve, reject) => {
        const checkClerk = setInterval(() => {
          if (typeof window.Clerk !== 'undefined') {
            clearInterval(checkClerk);
            resolve();
          }
        }, 100);
        setTimeout(() => {
          clearInterval(checkClerk);
          reject("Clerk failed to load");
        }, 10000);
      });
    }

    await window.Clerk.load({ debug: true });

    signInBtn.addEventListener('click', () => {
      window.Clerk.openSignIn({
        afterSignIn: () => handleUserAuthentication(window.Clerk.user)
      });
    });

    signUpBtn.addEventListener('click', () => {
      window.Clerk.openSignUp({
        afterSignUp: () => handleUserAuthentication(window.Clerk.user)
      });
    });

    signOutBtn.addEventListener('click', () => {
      window.Clerk.signOut();
      handleUserSignOut();
    });

    // Page protection
    const currentPage = window.location.pathname.replace(/^.*[\\/]/, '');
    if (pageAccessConfig[currentPage]) {
      if (!window.Clerk.user) {
        window.location.href = 'index.html'; // redirect if not logged in
        return;
      }
      if (!hasPageAccess(window.Clerk.user, currentPage)) {
        showAccessDenied();
        return;
      }
    }

    // Already signed in
    if (window.Clerk.user) {
      handleUserAuthentication(window.Clerk.user);
    }

    signInLoader.style.display = 'none';
    signUpLoader.style.display = 'none';
    signInBtn.disabled = false;
    signUpBtn.disabled = false;

  } catch (error) {
    console.error("Clerk init error:", error);
    showMessage("Authentication service unavailable.", "danger");
    signInLoader.style.display = 'none';
    signUpLoader.style.display = 'none';
    signInBtn.disabled = false;
    signUpBtn.disabled = false;
  }
}

// Admin panel link click interception
document.querySelectorAll('#admin-panel a').forEach(link => {
  link.addEventListener('click', (e) => {
    const targetPage = link.getAttribute('href');
    if (window.Clerk.user && !hasPageAccess(window.Clerk.user, targetPage)) {
      e.preventDefault();
      const accessDeniedModal = new bootstrap.Modal(document.getElementById('accessDeniedModal'));
      accessDeniedModal.show();
    }
  });
});

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadClerk);
} else {
  loadClerk();
}
