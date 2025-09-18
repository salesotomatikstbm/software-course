// Check authentication and role on page load
document.addEventListener('DOMContentLoaded', async function () {
  // Wait for Clerk to load
  if (typeof window.Clerk === 'undefined') {
    await new Promise((resolve) => {
      const checkClerk = setInterval(() => {
        if (typeof window.Clerk !== 'undefined') {
          clearInterval(checkClerk);
          resolve();
        }
      }, 100);
    });
  }

  // Load Clerk
  await window.Clerk.load();

  // If user is not authenticated, redirect to login page
  if (!window.Clerk.user) {
    window.location.href = 'index.html';
    return;
  }

  // Get user metadata
  const userMetadata = window.Clerk.user.publicMetadata || {};

  // Normalize roles → supports single "role" or multiple "roles"
  const userRoles = Array.isArray(userMetadata.roles)
    ? userMetadata.roles
    : [userMetadata.role || ''];

  // ✅ Required roles for this page
  const requiredRoles = ['ai']; // you can add more roles here if needed

  // Check if user has at least one of the required roles
  const hasAccess = requiredRoles.some(role => userRoles.includes(role));

  if (!hasAccess) {
    // Show access denied page
    document.body.innerHTML = `
      <div class="access-denied-container">
        <div class="access-denied">
          <div class="access-denied-icon">
            <i class="fas fa-ban"></i>
          </div>
          <h2>Access Denied</h2>
          <p>You need one of the following roles to access this page: 
            <strong>${requiredRoles.join(', ')}</strong>.<br>
            Your current roles are: <strong>${userRoles.filter(r => r).join(', ') || 'None'}</strong>
          </p>
          <a href="index.html" class="access-denied-btn">
            <i class="fas fa-arrow-left me-2"></i>Return to Dashboard
          </a>
        </div>
      </div>
    `;
    return;
  }

  // If user has the correct role, show user info
  const userEmail = window.Clerk.user.primaryEmailAddress?.emailAddress;
  const userName = window.Clerk.user.firstName || userEmail;

  document.getElementById('user-name').textContent = userName;

  // Properly set the user avatar
  const userAvatar = document.getElementById('user-avatar');
  if (window.Clerk.user.imageUrl) {
    userAvatar.src = window.Clerk.user.imageUrl;
  } else if (window.Clerk.user.profileImageUrl) {
    userAvatar.src = window.Clerk.user.profileImageUrl;
  } else {
    userAvatar.src = 'https://www.gravatar.com/avatar/?d=mp';
  }

  // Show the user info section
  document.getElementById('user-info').style.display = 'flex';

  // Add sign out functionality
  document.getElementById('sign-out-btn').addEventListener('click', () => {
    window.Clerk.signOut();
    window.location.href = '/';
  });
});
