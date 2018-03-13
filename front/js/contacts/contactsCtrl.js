(function() {
    'use strict';

    angular
        .module('contacts')
        .controller('contactsCtrl', contactsCtrl);

    function contactsCtrl($scope, $http, ContactsListFactory, ContactsByIdService) {
        onInitCtrl();

        function onInitCtrl(){
            ContactsListFactory.get().then(function(resp) {
                $scope.items = resp;
            });
        };

        $scope.title = 'Contacts'

        $scope.editContactState = false
        $scope.addContactState = false
        $scope.edit_status = ''
        $scope.checkboxStatus = function(add_reminder) {
            if (add_reminder) {
                return checked
            }
        };
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
            $scope.addContactState = false;
            var birthday2 = $scope.contact.birthday.toISOString().slice(0,10);
            $scope.contact.birthday = birthday2;
            ContactsByIdService.post($scope.contact).then(function(resp) {
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
            $scope.editContactState = false;
            var birthday2 = $scope.contact.birthday.toISOString().slice(0,10);
            $scope.contact.birthday = birthday2;
            ContactsByIdService.patch($scope.contact.id, $scope.contact).then(function(resp) {
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
        $scope.cancel = function() {
            $scope.editContactState = false
            $scope.addContactState = false
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


    }
})();