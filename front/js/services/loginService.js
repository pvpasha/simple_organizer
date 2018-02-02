(function() {
    'use strict';

    angular
        .module('Login')
        .service('AuthService', AuthService);

    function AuthService($http, $location, $localStorage, LoginReqFactory, VerifyTokenFactory) {
        var service = {};

        service.getToken = getToken;
        service.login = Login;
        service.logout = Logout;
        service.verify = VerifyToken;

        return service;

        function getToken(userdata) {
            LoginReqFactory.get(userdata).then(function(token) {
                $localStorage.currentUser = {
                    email: userdata.email,
                    token: token
                };
                $http.defaults.headers.common.Authotization = 'JWT ' + token; // Your Prefix Header;
            })
        }

        function Login(userdata) {
            getToken(userdata);
            $location.path('/');
            console.log('AuthService: Successfully logged!');
        }

        function Logout() {
            delete $localStorage.currentUser;
            $http.defaults.headers.common.Authotization = '';
            console.log('AuthService: Successfully logout!');
        }

        function VerifyToken(data) {
            VerifyTokenFactory.get(data)    // Add Fn If Error !!!
                .then(function(){
                    console.log('AuthService: Verify Token OK!');
                })
                .catch(function(error) {            //If Error Do this
                delete $localStorage.currentUser;
                $location.path('/login');
                console.error('AuthService: Verify Token ERROR!!!');
                })
        }
    }

})();