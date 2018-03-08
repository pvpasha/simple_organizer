(function(){
    'use strict';

    angular
        .module('password')
        .factory('PasswordListFactory', PasswordListFactory)
        .factory('PasswordByIdFactory', PasswordByIdFactory);

    function PasswordListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/password-organizer/list/')
                .then(function(response){
                    console.log('Get Password List OK!')
                    return response.data.results
                })
            }
        }
    }
    function PasswordByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/password-organizer/' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }

})();