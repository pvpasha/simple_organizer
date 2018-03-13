(function() {
    'use strict';

    angular
        .module('task')
        .filter('taskFinished', taskFinished);

    function taskFinished(){
        return function(data) {
            return data ? 'glyphicon glyphicon-plus' : 'glyphicon glyphicon-minus';
        }
    }

})();