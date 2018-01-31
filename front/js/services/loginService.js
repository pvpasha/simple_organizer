(function(){
    'use strict';

angular
    .module('Login')
    .service('AuthService', AuthService);

    function AuthService($http, $location, $localStorage, LoginReqFactory){
        var service = {};

        service.getToken = function(userdata) {
            LoginReqFactory.get(userdata)
            $localStorage.currentUser = {email:userdata.email, token:LoginReqFactory.get(userdata)};
            $http.defaults.headers.common.Authotization = 'JWT ' + $localStorage.currentUser.token
            $location.path('/')
            console.log('AuthService: ');

        }


    Login


        this.getLogout = function(){
            delete $localStorage.currentUser
//            $http.defaults.headers.common.Authotization = '' // ????
        }

    }

})();