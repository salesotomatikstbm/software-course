 function setActiveTabFromLocalStorage() {
    const activeTab = localStorage.getItem('activeTab');
    if (activeTab) {
      const activeTabButton = document.getElementById(activeTab);
      const tab = new bootstrap.Tab(activeTabButton); // Bootstrap 5 tab API
      tab.show(); // Show the active tab
    }
  }

  // Function to save the selected tab to localStorage
  function saveActiveTabToLocalStorage(event) {
    const activeTabId = event.target.id;
    localStorage.setItem('activeTab', activeTabId);
  }

  // Attach event listeners to each tab
  document.querySelectorAll('.nav-link').forEach(tabButton => {
    tabButton.addEventListener('click', saveActiveTabToLocalStorage);
  });

  // Set the active tab when the page loads
  window.onload = setActiveTabFromLocalStorage;





   // Basic password prompt for authentication
  function authenticateUser() {
    var password = prompt("Please enter the password to access this course:");
    var correctPassword = "scratch"; // Replace with your desired password

    if (password === correctPassword) {
      window.location.href = "./scratch/scratch.html"; // Redirect to course page
    } else {
      alert("Incorrect password. Access denied.");
    }
  }