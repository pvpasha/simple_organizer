(function() {
    'use strict';

    angular
        .module('Login')
        .service('AuthService', AuthService);

    function AuthService($http, $location, $localStorage, LoginReqFactory, VerifyTokenFactory, RefreshTokenFactory) {
        var service = {};

        service.getToken = getToken;
        service.login = Login;
        service.logout = Logout;
        service.verifyToken = VerifyToken;
        service.refreshToken = RefreshToken;
        service.checkLocalStorage = CheckLocalStorage;

        return service;

        function getToken(userdata) {
            LoginReqFactory.get(userdata).then(function(token) {
                $localStorage.currentUser = {
                    email: userdata.email,
                    token: token
                };
//                $http.defaults.headers.common.Authotization = 'JWT ' + token; // Your Prefix Header;
            })
        }

        function Login(userdata) {
            getToken(userdata);
            $location.path('/');
            console.log('AuthService: Successfully logged!');
        }

        function Logout() {
            delete $localStorage.currentUser;
//            $http.defaults.headers.common.Authotization = '';
            console.log('AuthService: Successfully logout!');
        }

        function VerifyToken(data) {
            VerifyTokenFactory.get(data)    // Add Fn If Error !!!
                .then(RefreshTokenFactory.get(data)
                    .then(function(resp){
                        $localStorage.currentUser = {
                            email: data.email,
                            token: resp
                        };
//                        $http.defaults.headers.common.Authotization = 'JWT ' + resp; // Your Prefix Header;
                        console.log('VerifyToken && AuthService: RefreshToken OK!');
                    })
                , function(error) {                                     //If Error Do this
//                delete $localStorage.currentUser;
//                $location.path('/login');
                console.log('AuthService: VerifyToken ERROR!', error.status);
                })
        }

        function RefreshToken(data) {
            RefreshTokenFactory.get(data)
                .then(function(resp){
                    $localStorage.currentUser = {
                    email: data.email,
                    token: resp
                };
//                $http.defaults.headers.common.Authotization = 'JWT ' + resp; // Your Prefix Header;
                    console.log('AuthService: RefreshToken OK!');
                })
        }

        function CheckLocalStorage(data) {
            if ($localStorage.currentUser){
                console.log('Wait checking your token!');
                VerifyToken(data);
            }else {
//                $location.path('/login');
                console.log('You DON"T Have currentUser, Please login!');
            }
        }

    }

})();