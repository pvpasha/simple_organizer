(function() {
    'use strict';

    angular
        .module('accounts')
        .factory('LoginReqFactory', LoginReqFactory)
        .factory('VerifyTokenFactory', VerifyTokenFactory)
        .factory('RefreshTokenFactory', RefreshTokenFactory)
        .factory('UserProfileFactory', UserProfileFactory)
        .factory('UpdateNameFactory', UpdateNameFactory)
        .factory('UpdateAvatarFactory', UpdateAvatarFactory)
        .factory('UpdateEmailFactory', UpdateEmailFactory);


    function LoginReqFactory($http, $location, $localStorage) {
        return {
            get: function(udata) {
                return $http.post('http://localhost:8000/token-auth/', udata)
                .then(function(response) {
                    console.log('LoginReqFactory OK!', response.status);
                    return response.data.token;
                })
            }
        }
    }
    function VerifyTokenFactory($http, $localStorage) {
        return {
            get: function(data) {
                return $http.post('http://localhost:8000/token-verify/', {token:data.token}) // Add Fn If Error ?!
                .then(function(response) {
                    console.log('VerifyTokenFactory OK!', response.status);
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
                .then(function(response) {
                   console.log('RefreshTokenFactory OK!', response.status);
                    return response.data.token
                }, function(error) {
                    delete $localStorage.currentUser;
                    $http.defaults.headers.common.Authorization = '';
                    console.log('RefreshTokenFactory Error!!!', error.status);
                })
            }
        }
    }
    function UserProfileFactory($http, $localStorage) {
        return {
            get: function(email) {
                return $http.get('http://localhost:8000/accounts/profile/' + email + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function UpdateNameFactory($http) {
        return {
            patch: function(email, name) {
                return $http.patch('http://localhost:8000/accounts/profile-name/' + email + '/', name)
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function UpdateAvatarFactory($http) {
        return {
            patch: function(email, file) {
                return $http.patch('http://localhost:8000/accounts/profile-avatar/' + email + '/', file)
                .then(function(response) {
                    console.log(response)
                    return response
                })
            }
        }
    }
    function UpdateEmailFactory($http) {
        return {
            patch: function(email, name) {
                return $http.patch('http://localhost:8000/accounts/profile-name/' + email + '/', name)
                .then(function(response) {
                    console.log(response.status)
                    return response.status
                })
            }
        }
    }

})();
