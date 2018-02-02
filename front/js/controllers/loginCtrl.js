(function() {
    'use strict';

    angular
        .module('Login')
        .controller('loginCtrl', loginCtrl);

    function loginCtrl($scope, $localStorage, AuthService) {
//        initCtrl();
//
//        function initCtrl(){
//            AuthService.verify($localStorage.currentUser);
//        }

        $scope.status = function() {
            if ($localStorage.currentUser) {
                return true
            } else {
                return false
            }
        };
        $scope.title = 'Login';
        $scope.userdata = {
            email: 'pvpasha@meta.ua',
            password: 'pasha123'
        }; //need delete this email & pass!!!
        $scope.logOut = function() {
            AuthService.logout();
        };
        $scope.logIn = function() {
            AuthService.login($scope.userdata);
            $scope.userdata = {};
        }
        $scope.verifyToken = function(){
            AuthService.verify($localStorage.currentUser);
        }
//        $scope.verifyToken = function(){
//            VerifyTokenFactory.get($localStorage.currentUser);
//        }

    }
})();