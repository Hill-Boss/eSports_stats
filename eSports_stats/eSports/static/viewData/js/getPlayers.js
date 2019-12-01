$(document).ready(function(){

  $.ajax(
    {
      type: 'GET',
      url: '/ajax/getGamePlayer/',

      success: function(response)
      {
        Options = document.getElementById('options')
        select = Options.innerHTML;
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
        Options.innerHTML = select;

      },

      failure: function()
      {
        alert("AJAX FAILED!");
      }
    }
  );
});
