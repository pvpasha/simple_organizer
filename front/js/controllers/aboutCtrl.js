(function(){
    'use strict';

angular
    .module('About')
    .controller('aboutCtrl', aboutCtrl);

    function aboutCtrl($scope) {
        this.title = 'SP - About';
    }

})();
