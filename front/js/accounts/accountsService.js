(function() {
    'use strict';

    angular
        .module('accounts')
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
            })
        }

        function Login(userdata) {
            getToken(userdata);
            $http.defaults.headers.common.Authorization = 'JWT ' + token;
            $location.path('/');
        }

        function Logout() {
            delete $localStorage.currentUser;
            $http.defaults.headers.common.Authorization = '';
            $location.path('/');
        }

        function VerifyToken(data) {
            VerifyTokenFactory.get(data)
                .then(RefreshTokenFactory.get(data)
                    .then(function(resp){
                        $localStorage.currentUser = {
                            email: data.email,
                            token: resp
                        };
                        $http.defaults.headers.common.Authorization = 'JWT ' + resp;
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
                $http.defaults.headers.common.Authorization = 'JWT ' + resp;
                console.log('AuthService: RefreshToken OK!');
                })
        }

        function CheckLocalStorage(data) {
            if ($localStorage.currentUser){
                console.log('Wait checking your token!');
                VerifyToken(data);
            }else {
                $location.path('/sing-in');
                console.log('You DON"T Have currentUser, Please login!');
            }
        }
    }

})();