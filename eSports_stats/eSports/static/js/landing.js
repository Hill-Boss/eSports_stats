function login() {
  email = document.getElementById('login_email').value;
  pswd = document.getElementById('login_pswd').value;
  console.log(email);
  console.log(pswd);
}

function signUp() {
  email = document.getElementById('signUp_email').value;
  pswd = document.getElementById('signUp_pswd').value;
  pswdR = document.getElementById('signUp_pswd_R').value;
}

function showDrop() {
  document.getElementById('myDropdown').classList.toggle("show");
}


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
