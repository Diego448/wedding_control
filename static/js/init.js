(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.slider').slider();
    $('.carousel.carousel-slider').carousel({
      fullWidth: true
    });
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

  }); // end of document ready
})(jQuery); // end of jQuery name space