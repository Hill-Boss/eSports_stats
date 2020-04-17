function getURL(game, username) {
  var outsidePage = document.getElementById('outsidePage');
  // TODO: This is probably illegal if it were public... but this is only until we have api calls/scrapping
  var url = '';
  if (game == 'Apex Legends') {
    url = "https://tracker.gg/apex/profile/origin/" + username + "/overview";
  } else if (game == 'Rocket League') {
    url = "https://rocketleague.tracker.network/profile/steam/" + username;
  } else if (game == 'Overwatch') {
    username = username.split('#');
    username = username[0] + '-' + username[1];
    url = "https://overwatchtracker.com/profile/pc/global/" + username;
  } else if (game == 'League of Legends') {
    url = "https://lol.mobalytics.gg/summoner/na/" + username + "/?season=13";
  }
  outsidePage.data = url;
  // document.getElementById('our-page').classList.toggle('hide');
  // outsidePage.classList.toggle('hide');
}
