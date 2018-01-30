(function(){
    'use strict';

angular
    .module('Home')
    .controller('homeCtrl', homeCtrl);

    function homeCtrl($scope){
        $scope.title = 'SP - Home';
        $scope.team = 'SP Lutsk';

        var date = new Date();    // Date
        $scope.today = date;
    }

})();





