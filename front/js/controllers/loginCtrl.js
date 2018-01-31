(function(){
    'use strict';

angular
    .module('Login')
    .controller('loginCtrl', loginCtrl);

    function loginCtrl($scope, $localStorage, AuthService){
        initCtrl();

        function initCtrl(){
            AuthService.logout();
        }

        $scope.status = function(){
            if ($localStorage.currentUser.email){
                return true
            }else {return false}
        };

        $scope.title = 'Login';
        $scope.userdata = {email: 'pvpasha@meta.ua', password: 'pasha123'}; //need delete this email & pass!!!
        $scope.logOut = function () {AuthService.logout();}
        $scope.logIn = function (){AuthService.login($scope.userdata); $scope.userdata = {};}

    }

})();