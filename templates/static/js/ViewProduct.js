$(document).ready(function() {
    $('.page-item').mouseover(function() {
      var newSrc = $(this).find('img').attr('src');
      $('#imageboxmain').attr('src', newSrc);
    });
  });