document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {onCloseEnd: function() {
        console.log('Modal closed!');
    }});
});