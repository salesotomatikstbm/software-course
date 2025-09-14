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





