(function(){
    'use strict';

angular
    .module('About')
    .controller('aboutCtrl', aboutCtrl);

    function aboutCtrl($scope) {
        $scope.title = 'SP - About';
    }

})();
