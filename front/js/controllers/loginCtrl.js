(function(){
    'use strict';

angular
    .module('Login', ['ngStorage'])
    .controller('loginCtrl', loginCtrl);

    function loginCtrl($scope, $http, $localStorage, LoginReqFactory, LogoutReqFactory){
        $scope.title = 'Login';
        $scope.userdata = {};
        $scope.logIn = function () {LoginReqFactory.get($scope.userdata);}
        $scope.logOut = function () {LogoutReqFactory.get();}
    }

})();