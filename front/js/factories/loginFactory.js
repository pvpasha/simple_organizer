(function(){
    'use strict';

angular
    .module('Login')
    .factory('LoginReqFactory', LoginReqFactory)
//    .factory('LogoutReqFactory', LogoutReqFactory)

    function LoginReqFactory($http, $window, $location, $localStorage){
        return {
            get: function(userdata) {
                return $http.post('http://localhost:8000/api-token-auth/', userdata)
                .then(function successCallback (response){
//                    $localStorage.currentUser = {email: userdata.email, token: response.data.token}
//                    $http.defaults.headers.common.Authotization = 'JWT ' + response.data.token
//                    $location.path('/')
                    token = response.data.token;
                    //return token //?????????????
                    console.log('LoginReqFactory: ', token);

                    },
                    function errorCallback() {$window.alert('Your email or password are incorrect!');})
            }
        }
    }

//    function LogoutReqFactory($http, $localStorage){
//        return {
//            get: function() {
//                delete $localStorage.currentUser
//                $http.defaults.headers.common.Authotization = '' // ????
//            }
//        }
//    }

})();