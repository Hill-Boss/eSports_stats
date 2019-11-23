$(document).ready(function(){
  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getGamePlayer/',

      success: function(response)
      {
        Options = document.getElementById('options')
        select = '<select name="Game">';
        for (var key in response) {
          optgroup = '<optgroup label=\"' + key + '\">';
          for (var i = 0; i < response[key].length; i++) {
            value = response[key][i];
            option = '<option value=\"' + (key+','+value) + '\">' + value + '</option>';
            optgroup += option;
          }
          optgroup += '</optgroup>';

          console.log(optgroup);
          select += optgroup;
        }
        select += '<input type="submit" onclick="getURL()"></select>';
        Options.innerHTML = select;

      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});
