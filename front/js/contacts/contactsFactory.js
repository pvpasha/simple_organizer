(function(){
    'use strict';

    angular
        .module('contacts')
        .factory('ContactsListFactory', ContactsListFactory)
        .factory('ContactsByIdFactory', ContactsByIdFactory);

    function ContactsListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/contacts/list/')
                .then(function(response){
                    console.log('Get Contact List OK!')
                    return response.data.results
                })
            }
        }
    }
    function ContactsByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/contacts/' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
})();