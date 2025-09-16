
    // Check authentication and role on page load
    document.addEventListener('DOMContentLoaded', async function() {
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
      
      // Check if user has the required role for this page
      // For coding.html, we require the 'teacher' role
      if (userMetadata.role !== 'ai') {
        // Show access denied page
        document.body.innerHTML = `
          <div class="access-denied-container">
            <div class="access-denied">
              <div class="access-denied-icon">
                <i class="fas fa-ban"></i>
              </div>
              <h2>Access Denied</h2>
              <p>You need the <strong>Teacher</strong> role to access this page. Your current role is: <strong>${userMetadata.role || 'None'}</strong></p>
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
      
      // FIXED: Properly set the user avatar
      const userAvatar = document.getElementById('user-avatar');
      if (window.Clerk.user.imageUrl) {
        userAvatar.src = window.Clerk.user.imageUrl;
      } else if (window.Clerk.user.profileImageUrl) {
        // Fallback to profileImageUrl if imageUrl doesn't exist
        userAvatar.src = window.Clerk.user.profileImageUrl;
      } else {
        // Show a default avatar if no image is available
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
