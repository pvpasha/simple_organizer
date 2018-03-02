(function() {
    'use strict';

    angular
        .module('accounts')
        .factory('LoginReqFactory', LoginReqFactory)
        .factory('VerifyTokenFactory', VerifyTokenFactory)
        .factory('RefreshTokenFactory', RefreshTokenFactory);

    function LoginReqFactory($http, $location, $localStorage) {
        return {
            get: function(udata) {
                return $http.post('http://localhost:8000/token-auth/', udata)
                .then(function(resp) {
                    console.log('LoginReqFactory OK!', resp.status);
                    return resp.data.token;
                })
            }
        }
    }

    function VerifyTokenFactory($http, $localStorage) {
        return {
            get: function(data) {
                return $http.post('http://localhost:8000/token-verify/', {token:data.token}) // Add Fn If Error ?!
                .then(function(resp) {
                    console.log('VerifyTokenFactory OK!', resp.status);
                }, function(error) {
                    console.log('VerifyTokenFactory Error!', error.status);
                    return error.status
                })
           }
        }
    }

    function RefreshTokenFactory($http, $localStorage) {
        return {
            get: function(data) {
                return $http.post('http://localhost:8000/token-refresh/', {token:data.token})
                .then(function(resp) {
                   console.log('RefreshTokenFactory OK!', resp.status);
                    return resp.data.token
                }, function(error) {
                    console.log('RefreshTokenFactory Error!', error.status);
                    return error.status
                })
            }
        }
    }

})();
