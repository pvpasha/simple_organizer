(function() {
    'use strict';

// --myapp.main--
angular.module('myapp.main', ['ngRoute'])

//Routing
    .config(['$routeProvider', function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl:'templates/home.html',
                controller:'myapp.MainCtrl',
                controllerAs: 'main'
            })
            .when('/login', {
                templateUrl:'templates/login.html',
                controller:'myapp.LoginCtrl',
                controllerAs: 'login'
            })
            .when('/about', {
                templateUrl:'templates/about.html',
                controller:'myapp.AboutCtrl',
                controllerAs: 'about'
            })
            .otherwise({
                redirectTo: '/'
            });
    }])

//Main Controller
    .controller('myapp.MainCtrl', ['$scope', '$http', function($scope, $http) {
        $scope.title = 'Simple Organizer';
        $scope.team = 'SP Lutsk';

        $http.get('js/user.json').then(function(response) {
          $scope.users = response.data;
        });

        var date = new Date();    // Date
        $scope.today = date;

    }]);

// --myapp.login--
angular.module('myapp.login', ['ngStorage'])

////
    .factory('LoginReqFactory', LoginReqFactory)
    .factory('LogoutReqFactory', LogoutReqFactory)


    .service('Auth', function($http) {

        this.login = function ($scope) {
//            var userdata = {
//
//            };          //user data (login+password)

            var req = {
                method: 'POST',
                url: 'http://localhost:8000/api-token-auth/',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: {
                    'email': 'pvpasha@meta.ua',
                    'password': 'pasha123'
                }
            };
            console.log('Your POST data: ', req.data);

            $http(req).then(function (response) {
                var tokenUsers = response.data;
                var serialResp = JSON.stringify(tokenUsers.token);
                localStorage.setItem('aUser-token', serialResp);

                var serialResp1 = JSON.stringify(tokenUsers.email);
                localStorage.setItem('aUser-email', serialResp1);

            });
        };

        this.logout = function() {
            localStorage.removeItem('aUser-token')
            localStorage.removeItem('aUser-email')
            console.log('localStorage are cleared');
            // localStorage.clear();
            // var returnResp = JSON.parse(localStorage.getItem('aUser-token'))
        };
    })

    //Login Controller
    .controller('myapp.LoginCtrl', ['$scope', '$http', '$localStorage', '$location', 'LoginReqFactory', 'LogoutReqFactory', function($scope, $http, $location, $localStorage, LoginReqFactory, LogoutReqFactory) {

        $scope.title = 'Login';

        $scope.userdata = {};

        $scope.logIn = function () {LoginReqFactory.get($scope.userdata);}
        $scope.logOut = function () {LogoutReqFactory.get();}

//        $rootScope.userdata = {
//            'email': $scope.email,
//            'password': $scope.password
//        };

}]);
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


// --myapp.about--
angular.module('myapp.about', [])

//About Controller
    .controller('myapp.AboutCtrl', ['$scope', function($scope) {

        $scope.title = 'About';

        // console.log(title);
}]);

// --myapp--
angular.module('myapp', [
    'myapp.main',
    'myapp.login',
    'myapp.about'
]);
})();