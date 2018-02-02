(function() {
    'use strict';

    angular
        .module('Login')
        .factory('LoginReqFactory', LoginReqFactory)
        .factory('VerifyTokenFactory', VerifyTokenFactory);

    function LoginReqFactory($http, $location, $localStorage) {
        return {
            get: function(userdata) {
                return $http.post('http://localhost:8000/api-token-auth/', userdata)
                    .then(function(response) {
                        console.log('LoginReqFactory OK!');
                        return response.data.token;
                    })
            }
        }
    }

    function VerifyTokenFactory($http, $localStorage) {
        return {
            get: function(data) {
                return $http.post('http://localhost:8000/api-token-verify/', {token:data.token}) // Add Fn If Error !!!
                    .then(function(response) {
                        console.log('VerifyTokenFactory OK!');
                        return response.data.token;
                    })
            }
        }
    }

})();