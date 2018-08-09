(function() {
    'use strict';

    angular
        .module('password')
        .service('PasswordByIdService', PasswordByIdService);

    function PasswordByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/password-organizer/create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/password-organizer/list/')
                        .then(function(response){
                            console.log('Created password & update PasswordList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/password-organizer/' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/password-organizer/list/')
                        .then(function(response){
                            console.log('Updated password & update PasswordList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/password-organizer/' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/password-organizer/list/')
                        .then(function(response){
                            console.log('Deleted password & update PasswordList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }

})();