(function() {
    'use strict';

    angular
        .module('Login')
        .controller('loginCtrl', loginCtrl);

    function loginCtrl($scope, $http, $localStorage, AuthService, VerifyTokenFactory, RefreshTokenFactory) {
//        initCtrl();
//
//        function initCtrl(){
//            AuthService.checkLocalStorage($localStorage.currentUser);
//        };

        this.title = 'Login';
        $scope.userdata = {
            email: '',                                           //need delete this email & pass!!!
            password: ''
        };

        $scope.username = function() {
            if ($localStorage.currentUser){
                return $localStorage.currentUser.email
            } else {
                return 'Anonymous'
            }
        }

        $scope.logFacebook = function() {
            $http.get('http://localhost:8000/api-auth/login/facebook/')
        };

        $scope.verifyTokenS = function(){
            AuthService.verifyToken($localStorage.currentUser);
        };
        $scope.verifyTokenF = function(){
            VerifyTokenFactory.get($localStorage.currentUser);
        };
        $scope.verifyToken = function(){                                        //delete this fn!
            AuthService.checkLocalStorage($localStorage.currentUser);
        };
        $scope.refreshTokenS = function(){
        AuthService.refreshToken($localStorage.currentUser);
        };
        $scope.refreshTokenF = function(){
            RefreshTokenFactory.get($localStorage.currentUser);
        };

        $scope.status = function() {

            if (AuthService.checkLocalStorage($localStorage.currentUser)) {
                return 'Hello, ', $localStorage.currentUser.email
            } else {
                return 'Please login'
            }
        };

        $scope.currentu = function() {
            if ($localStorage.currentUser){
            }
        };

        $scope.logIn = function() {
            AuthService.login($scope.userdata);
            $scope.userdata = {};
        };

        $scope.logOut = function() {
            AuthService.logout();
        };

    }
})();
