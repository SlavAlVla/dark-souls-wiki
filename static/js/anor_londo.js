function change_style(y, h) {
    if ($(window).scrollTop() < y - 300 || $(window).scrollTop() > y+h) {
      $('body').css('background-image', 'url("/static/images/locations/anor_londo.png")');
      $('main').css('background-color', 'rgba(83, 57, 40, .75)');
      $('.block').css('background-color', 'rgba(99, 73, 56, .75)');
      $('footer').css('background-color', 'rgb(83, 57, 40)');
    } else {
      $('body').css('background-image', 'url("/static/images/locations/dark_anor_londo.jpg")');
      $('main').css('background-color', 'rgba(12, 30, 36, .75)');
      $('.block').css('background-color', 'rgba(28, 46, 52, .75)');
      $('footer').css('background-color', 'rgb(12, 30, 36)');
    }
  }
  
  var y = $('#dark_anor_londo').position().top;
  var h = $('#dark_anor_londo').height();

  $(window).scroll(function() {
    change_style(y, h);
  });