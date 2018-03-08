(function() {
    'use strict';

    angular
        .module('contacts')
        .controller('contactsCtrl', contactsCtrl);

    function contactsCtrl($scope, $http, ContactsListFactory, ContactsByIdService) {
        initCtrl();

        function initCtrl(){
            ContactsListFactory.get().then(function(resp) {
                $scope.items = resp;
            });
        };

        this.title = 'Contacts'

        $scope.editContactState = false
        $scope.addContactState = false
        $scope.edit_status = ''

        $scope.listContacts = function() {
            ContactsListFactory.get().then(function(resp) {
                $scope.items = resp;
            });
        };
        $scope.contact = {
            name: '',
            surname: '',
            phone: '',
            email_address: '',
            home_address: '',
            birthday: '',
            add_reminder: false
        };
        $scope.addContact = function() {
            $scope.addContactState = true
            $scope.edit_status = 'Add Form'
        }
        $scope.editContact = function(contact) {
            var birthday = new Date(contact.birthday)
            $scope.contact = contact
            $scope.contact.birthday = birthday
            $scope.editContactState = true
            $scope.edit_status = 'Edit Form'
        }
        $scope.createItem = function() {
            console.log($scope.contact);
            $scope.addContactState = false;
            ContactsByIdService.post($scope.contact).then(function(resp) {  //TODO: TypeError: date !!!
                $scope.items = resp;
            });
            $scope.contact = {
                name: '',
                surname: '',
                phone: '',
                email_address: '',
                home_address: '',
                birthday: '',
                add_reminder: false
            };
        };
        $scope.editItem = function() {
            console.log($scope.contact);
            $scope.editContactState = false;
            ContactsByIdService.patch($scope.contact.id, $scope.contact).then(function(resp) {  //TODO: TypeError: date !!!
                $scope.items = resp;
            });
            $scope.contact = {
                name: '',
                surname: '',
                phone: '',
                email_address: '',
                home_address: '',
                birthday: '',
                add_reminder: false
            };
        };
        $scope.delete = function(id) {
            ContactsByIdService.delete(id).then(function(resp) {
                $scope.items = resp;
            });
        };

    }
})();