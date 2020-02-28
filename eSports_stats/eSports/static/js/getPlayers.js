$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getGamePlayer/',

      success: function(response)
      {
        div = document.getElementById('games-players');

        select = div.innerHTML;
        var id = 0;
        for (var key in response) {
          game = "<div id= 'game-" + id + "' class=\"player-button teal w-100per\" onclick=\"document.getElementById('players-" + id + "').classList.toggle('hide')\"><h6>" + key + "</h6></div>";
          players = "<div id=\"players-" + id + "\" class=\"w3-white hide\">";
          id = id + 1;
          for (var i = 0; i < response[key].length; i++) {
            value = response[key][i];
            player = "<div class=\"w3-btn w3-hover-light-green\" style=\"width: 100%;\" onclick=\"getURL('" + key + "\',\'" + value + "')\">" + value + "</div>"
            players += player;
          }
          game += players + '</div>';
          select += game;
        }
        div.innerHTML = select;
        // Options.innerHTML = select;

      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});


// $(document).ready(function(){
//
//   $.ajax(
//     {
//       type: 'GET',
//       url: '/ajax/getGamePlayer/',
//
//       success: function(response)
//       {
//         Options = document.getElementById('options')
//         select = Options.innerHTML;
//         for (var key in response) {
//           optgroup = '<optgroup label=\"' + key + '\">';
//           for (var i = 0; i < response[key].length; i++) {
//             value = response[key][i];
//             option = '<option value=\"' + (key+','+value) + '\">' + value + '</option>';
//             optgroup += option;
//           }
//           optgroup += '</optgroup>';
//
//           console.log(optgroup);
//           select += optgroup;
//         }
//         Options.innerHTML = select;
//
//       },
//
//       failure: function()
//       {
//         alert("AJAX FAILED!");
//       }
//     }
//   );
// });
