(function() {
    'use strict';

    angular
        .module('accounts')
        .controller('accountsCtrl', accountsCtrl);

    function accountsCtrl($scope, $http, $localStorage, AuthService, RefreshTokenFactory, UserProfileFactory,
                            UpdateNameFactory) {
        initCtrl();

        function initCtrl(){
            AuthService.checkLocalStorage($localStorage.currentUser);
        };

        this.title = 'SP - Home';

        $scope.team = 'SP Team';
        $scope.brand = 'Simple Organizer';
        $scope.version = 'beta 0.01';
        $scope.today = new Date();

        $scope.userdata = {
            email: 'pvpasha@meta.ua',
            password: 'pasha123'
        };
        $scope.username = function() {
            if ($localStorage.currentUser){
                return $localStorage.currentUser.email;
            }
        };
        $scope.status_user = function() {
            if ($localStorage.currentUser){
                return true;
            }
        };
        $scope.logIn = function() {
            AuthService.Login($scope.userdata);
            $scope.userdata = {};
        };
        $scope.logOut = function() {
            AuthService.Logout();
        };
        $scope.userProfile = function() {
            UserProfileFactory.get($localStorage.currentUser.email).then(function(resp) {
                $scope.item = resp;
            });
        };
        $scope.new_name = {
                username: '',
                second_name: ''
        };
        $scope.updateName = function() {
            UpdateNameFactory.patch($localStorage.currentUser.email, $scope.new_name);
        };
        $scope.updateEmail = function() {
            UpdateEmailFactory.patch($localStorage.currentUser.email, $scope.new_email);
        }



    }
})();
