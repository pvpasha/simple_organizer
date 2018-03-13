(function() {
    'use strict';

    angular
        .module('budget')
        .filter('transactionType', transactionType);

    function transactionType(){
        return function(data) {
            return data ? 'glyphicon glyphicon-log-in' : 'glyphicon glyphicon-log-out';
        }
    }

})();