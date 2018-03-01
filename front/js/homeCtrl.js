(function(){
    'use strict';

angular
    .module('home')
    .controller('homeCtrl', homeCtrl);

    function homeCtrl($scope){
        this.title = 'SP - Home';
        $scope.team = 'SP Lutsk';
        $scope.brand = 'Simple Organizer'

        var date = new Date();
        $scope.today = date;
    }

})();





