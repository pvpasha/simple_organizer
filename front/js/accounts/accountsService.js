(function() {
    'use strict';

    angular
        .module('accounts')
        .service('AuthService', AuthService);

    function AuthService($http, $location, $localStorage, LoginReqFactory, VerifyTokenFactory, RefreshTokenFactory) {
        var service = {};

        service.getToken = getToken;
        service.Login = Login;
        service.Logout = Logout;
        service.verifyToken = VerifyToken;
        service.refreshToken = RefreshToken;
        service.checkLocalStorage = CheckLocalStorage;
        service.SignUp = SignUp;

        return service;

        function getToken(userdata) {
            LoginReqFactory.get(userdata)
                .then(function(token) {
                    $localStorage.currentUser = {
                        email: userdata.email,
                        token: token
                    };
                    $http.defaults.headers.common.Authorization = 'JWT ' + token;
                })
        }

        function Login(userdata) {
            getToken(userdata);
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
                    }),
                    function(error) {
//                        delete $localStorage.currentUser;
//                        $location.path('/login');
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
                }, function(error) {
                    delete $localStorage.currentUser;
                    $http.defaults.headers.common.Authorization = '';
                    console.log('RefreshToken Error!!!', error.status);
                    return error.status
                })
        }
        function CheckLocalStorage(data) {
            if ($localStorage.currentUser){
                RefreshToken(data);
            }else {
                delete $localStorage.currentUser;
            }
        }
        function SignUp(data) {
            $http.post('http://localhost:8000/accounts/sing-up/', data)
                .then(function(response){
                    console.log('SignUp OK!!', response.status);
                    $location.path('/sing-in');
                    return response.status
                });


        }
    }
})();