function showDrop() {
  document.getElementById('myDropdown').classList.toggle("show");
}


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.drop')) {
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
// var Players = {
//   Apex: [
//     "VaccaFlacca",
//     "JayX",
//     "Blitz"
//   ],
//   LeagueOfLegends: [
//     "Vegikarp",
//     "Wish",
//     "Aimbot.exe"
//   ],
//   RocketLeague: [
//     "KogtreyFu",
//     "Soul",
//     "VaccaFlacca"
//   ]
// }
//
// function dropPlayers(Game){
//
//   var div = document.getElementById(Game);
//
//   for (var i = 0; i < Players[Game].length; i++) {
//     Player = Players[Game][i];
//     var button = document.createElement("Button");
//     button.style.width = '100%';
//     button.classList.add("player-button");
//     var playerName = document.createTextNode(Player);
//     button.appendChild(playerName);
//     div.appendChild(button);
//   }
// }

function dropPlayers(Game){

  var div = document.getElementById(Game);

  for (var i = 0; i < Players[Game].length; i++) {
    Player = Players[Game][i];
    var button = document.createElement("Button");
    button.style.width = '100%';
    button.classList.add("player-button");
    var playerName = document.createTextNode(Player);
    button.appendChild(playerName);
    div.appendChild(button);
  }
}
