(function() {
    'use strict';

    angular
        .module('accounts')
        .controller('accountsCtrl', accountsCtrl);

    function accountsCtrl($scope, $http, $localStorage, AuthService, RefreshTokenFactory, UserProfileFactory,
                            UpdateNameFactory, UpdateAvatarFactory, UpdateEmailFactory) {
        onInitCtrl();

        function onInitCtrl(){
            AuthService.checkLocalStorage($localStorage.currentUser);
        };

        this.title = 'SP - Home';

        $scope.team = 'SP Team';
        $scope.brand = 'Simple Organizer';
        $scope.version = 'beta 0.01';
        $scope.today = new Date();
        $scope.change_name_state = false;
        $scope.change_email_state = false;
        $scope.change_password_state = false;

        $scope.userData = {
            email: '',
            password: ''
        };
        $scope.userEmail = function() {
            if ($localStorage.currentUser){
                return $localStorage.currentUser.email;
            };
        };
        $scope.logIn = function() {
            AuthService.Login($scope.userData);
            $scope.userData = {};
        };
        $scope.logOut = function() {
            AuthService.Logout();
        };
        $scope.dataSignUp = {
            email: '',
            username: '',
            password1: '',
            password2: ''
        };
        $scope.signUp = function() {
            if ($scope.dataSignUp.password1 == $scope.dataSignUp.password2) {
                AuthService.SignUp($scope.dataSignUp);
                $scope.dataSignUp = {};
            } else {
                alert('Please check your passwords. Passwords MUST be identical!');
            };
        };
        $scope.userProfile = function() {
            UserProfileFactory.get($localStorage.currentUser.email).then(function(user) {
                $scope.userCurrent = user;
            });
        };
        $scope.changeAvatar = function() {
            $scope.change_name_state = false;
            $scope.change_email_state = false;
            $scope.change_password_state = false;
            var selectedFile = document.getElementById('avatar').file;
            var avatar = {'avatar': selectedFile}
            console.log(selectedFile)
            UpdateAvatarFactory.patch($localStorage.currentUser.email, avatar).then(function(user) {
                $scope.userCurrent = user;
                });
        };
        $scope.changeName = function() {
            $scope.change_name_state = true;
            $scope.change_email_state = false;
            $scope.change_password_state = false;
            $scope.newName = {
                username: $scope.userCurrent.username,
                second_name: $scope.userCurrent.second_name
            };
        };
        $scope.updateName = function() {
            $scope.change_name_state = false;
            UpdateNameFactory.patch($localStorage.currentUser.email, $scope.newName).then(function(user) {
                $scope.userCurrent = user;
            });
        };
        $scope.changeEmail = function() {
            $scope.change_email_state = true;
            $scope.change_name_state = false;
            $scope.change_password_state = false;
//            UpdateEmailFactory.patch($localStorage.currentUser.email, $scope.new_email);
            // TODO: change email!
//            UserProfileFactory.get($localStorage.currentUser.email).then(function(user) {
//                $scope.userCurrent = user;
//            });
        };
        $scope.changePassword = function() {
            $scope.change_name_state = false;
            $scope.change_email_state = false;
            $scope.change_password_state = true;
            // TODO: change password!
//            UserProfileFactory.get($localStorage.currentUser.email).then(function(user) {
//                $scope.userCurrent = user;
//            });
        };
        $scope.changeCancel = function() {
            $scope.change_name_state = false;
            $scope.change_email_state = false;
            $scope.change_password_state = false;
        };

    }
})();
