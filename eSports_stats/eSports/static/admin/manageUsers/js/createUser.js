function isPlayer() {
  if (document.getElementsByName('Player')[0].checked) {
    document.getElementById('player').style.display = 'block';
  } else {
    document.getElementById('player').style.display = 'none';
  }
}

function isStaff() {
  if (document.getElementsByName('Staff')[0].checked) {
    document.getElementById('staff').style.display = 'block';
  } else {
    document.getElementById('staff').style.display = 'none';
  }
}
