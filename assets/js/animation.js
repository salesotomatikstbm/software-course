
    // Check if user is already authenticated
    if (sessionStorage.getItem('otomatiks_authenticated') === 'true') {
      // Redirect to admin page if already logged in
      window.location.replace('admin.html');
    }

    document.addEventListener('DOMContentLoaded', function() {
      // Handle form submission
      document.getElementById('loginForm').addEventListener('submit', function(e) {
        e.preventDefault();
        validateLogin();
      });
    });

    function validateLogin() {
      // Get current date and time components
      const currentDate = new Date();
      const currentDay = String(currentDate.getDate()).padStart(2, '0');
      const currentMonth = String(currentDate.getMonth() + 1).padStart(2, '0');
      const currentYear = currentDate.getFullYear();
      const currentHour = String(currentDate.getHours()).padStart(2, '0');
      
      // Create the expected password
      const dynamicPassword = `${currentDay}/${currentMonth}/${currentYear}/${currentHour}`;
      
      // Get user input
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;
      
      // Validate credentials
      if (username === "otomatiks" && password === dynamicPassword) {
        // Set authentication flag
        sessionStorage.setItem('otomatiks_authenticated', 'true');
        
        // Successful login - redirect to admin page with replacement
        window.location.replace('admin.html');
      } else {
        // Show error message
        const errorElement = document.getElementById("error-message");
        errorElement.textContent = "Invalid username or password!";
        errorElement.style.display = "block";
        
        // Shake animation for error feedback
        const card = document.querySelector('.card');
        card.classList.add('animate__animated', 'animate__headShake');
        setTimeout(() => {
          card.classList.remove('animate__animated', 'animate__headShake');
        }, 1000);
      }
    }
