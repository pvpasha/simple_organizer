(function() {
    'use strict';

    angular
        .module('contacts')
        .service('ContactsByIdService', ContactsByIdService);

    function ContactsByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/contacts/create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/contacts/list/')
                        .then(function(response){
                            console.log('Created contact & update ContactList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/contacts/' + id + '/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/contacts/list/')
                        .then(function(response){
                            console.log('Updated contact & update ContactList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/contacts/' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/contacts/list/')
                        .then(function(response){
                            console.log('Deleted contact & update ContactList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }
})();