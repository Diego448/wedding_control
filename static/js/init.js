(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.slider').slider();
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);

    instances.pause();
    instances.start();
    instances.next();
    instances.prev();

  }); // end of document ready
})(jQuery); // end of jQuery name space