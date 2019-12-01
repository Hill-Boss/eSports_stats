function getURL() {
  var outsidePage = document.getElementById('outsidePage');
  var data_game = document.getElementsByName('Game')[0].value;
  data_game = data_game.split(",");
  var url = '';
  if (data_game[0] == 'Apex Legends') {
    url = apex_url(data_game[1]);
  } else if (data_game[0] == 'Rocket League') {
    url = rl_url(data_game[1]);
  } else if (data_game[0] == 'Overwatch') {
    url = ow_url(data_game[1]);
  } else if (data_game[0] == 'League of Legends') {
    url = lol_url(data_game[1]);
  } else {
    url = '';
  }
  outsidePage.data = url;
  outsidePage.style.display = "block";
}
// TODO: This is probably illegal if it were public... but this is only until we have api calls/scrapping
function apex_url(data) {
  var url = "https://tracker.gg/apex/profile/origin/" + data + "/overview";
  return url;
}
function rl_url(data) {
  var url = "https://rocketleague.tracker.network/profile/steam/" + data;
  return url;
}
function ow_url(data) {
  data = data.split('#');
  data = data[0] + '-' + data[1];
  var url = "https://overwatchtracker.com/profile/pc/global/" + data;
  return url;
}
function lol_url(data) {
  var url = "https://lol.mobalytics.gg/summoner/na/" + data + "/?season=13";
  return url;
}
