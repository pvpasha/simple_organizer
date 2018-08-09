(function() {
    'use strict';

    angular
        .module('contacts')
        .filter('addReminder', addReminder);

    function addReminder(){
        return function(data) {
            return data ? 'glyphicon glyphicon-ok' : 'glyphicon glyphicon-minus';
        }
    }

})();