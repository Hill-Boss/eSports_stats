// Get the Sidebar
var Sidebar = document.getElementById("Sidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("Overlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function sidebar_open() {
  if (Sidebar.style.display === 'block') {
    Sidebar.style.display = 'none';
    overlayBg.style.display = "none";
  } else {
    Sidebar.style.display = 'block';
    overlayBg.style.display = "block";
  }
}

// Close the sidebar with the close button
function sidebar_close() {
  Sidebar.style.display = "none";
  overlayBg.style.display = "none";
}
