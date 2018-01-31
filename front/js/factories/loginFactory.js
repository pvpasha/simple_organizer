(function(){
    'use strict';

angular
    .module('Login')
    .factory('LoginReqFactory', LoginReqFactory)

    function LoginReqFactory($http, $window, $location, $localStorage){
        return {
            get: function(userdata) {
                return $http.post('http://localhost:8000/api-token-auth/', userdata)
                .then (function (response){
                    console.log('LoginReqFactory: ', response.data.token);
                    return response.data.token;})
            }
        }
    }

})();