(function(){
    'use strict';

angular
    .module('Login')
    .service('AuthService', AuthService);

    function AuthService($http, $location, $localStorage, LoginReqFactory){
        var service = {};


        service.getToken = getToken;
        service.login = Login;
        service.logout = Logout;

        return service;
        function getToken(userdata) {
            LoginReqFactory.get(userdata).then (function(token){
                $localStorage.currentUser = {email:userdata.email, token:token};
                $http.defaults.headers.common.Authotization = 'JWT ' + token
            })



        }

        function Login(userdata){
            getToken(userdata)
             $location.path('/')
            console.log('AuthService: Succssesfully loginned!!');
        }
        function Logout(){
            delete $localStorage.currentUser
            $http.defaults.headers.common.Authotization = '';
            console.log('AuthService: Succssesfully logouted');
        }

    }

})();