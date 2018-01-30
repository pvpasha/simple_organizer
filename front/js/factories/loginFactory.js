(function(){
    'use strict';

angular
    .module('Login')
    .factory('LoginReqFactory', LoginReqFactory)
    .factory('LogoutReqFactory', LogoutReqFactory)

    function LoginReqFactory($http, $localStorage, $location){
        return {
            get: function(userdata) {
                return $http.post('http://localhost:8000/api-token-auth/', userdata)
                .then(function(response) {
                    if (response.data.token) {
                        $localStorage.currentUser = {email: userdata.email, token: response.data.token}
                        $http.defaults.headers.common.Authotization = 'JWT ' + response.data.token
                        $location.path('')
                        // callback (true)
                    }
                })
                // .error(function() {callback (false)})
            }
        }
    }

    function LogoutReqFactory($http, $localStorage){
        return {
            get: function() {
                delete $localStorage.currentUser
                $http.defaults.headers.common.Authotization = ''
            }
        }
    }

})();