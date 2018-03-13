(function() {
    'use strict';

    angular
        .module('password')
        .controller('passwordCtrl', passwordCtrl);

    function passwordCtrl($scope, $http, PasswordListFactory, PasswordByIdService) {

        initCtrl();

        function initCtrl(){
            PasswordListFactory.get().then(function(resp) {
                $scope.items = resp;
            });
        };

        this.title = 'Password'

        $scope.editPasswordState = false;
        $scope.addPasswordState = false;
        $scope.edit_status = '';

        $scope.password = {
            resource_url: '',
            password_res: ''
        };
        $scope.listPassword = function() {
            PasswordListFactory.get().then(function(resp) {
                $scope.items = resp;
            });
        };
        $scope.addPassword = function() {
            $scope.addPasswordState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editPassword = function(password) {
            $scope.password = password;
            $scope.editPasswordState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createPassword = function() {
            $scope.addPasswordState = false;
            PasswordByIdService.post($scope.password).then(function(resp) {
                $scope.items = resp;
            });
            $scope.password = {
                resource_url: '',
                password_res: ''
            };
        };
        $scope.updatePassword = function() {
            $scope.editPasswordState = false;
            PasswordByIdService.patch($scope.password.id, $scope.password).then(function(resp) {
                $scope.items = resp;
            });
            $scope.password = {
                resource_url: '',
                password_res: ''
            };
        };
        $scope.deletePassword = function(id) {
            PasswordByIdService.delete(id).then(function(resp) {
                $scope.items = resp;
            });
        };
        $scope.cancel = function() {
            $scope.editPasswordState = false
            $scope.addPasswordState = false
            $scope.password = {
                resource_url: '',
                password_res: ''
            };
        };

    }
})();