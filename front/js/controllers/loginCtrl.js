(function(){
    'use strict';

angular
    .module('Login')
    .controller('loginCtrl', loginCtrl);

    function loginCtrl($scope, AuthService){
        $scope.title = 'Login';
        $scope.userdata = {email: 'pvpasha@meta.ua', password': 'pasha123'}; //need delete this email & pass!!!
        //$scope.logIn = function () {LoginReqFactory.get($scope.userdata);}
        //$scope.logOut = function () {LogoutReqFactory.get();};
        $scope.logOut = function () {AuthService.getLogout();}
        $scope.logIn = function (){AuthService.getLogin($scope.userdata); $scope.userdata = {};}

    }

})();