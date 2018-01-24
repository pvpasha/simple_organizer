(function() {
    'use strict';

// --myapp.main--
angular.module('myapp.main', ['ngRoute'])

//Routing
    .config(['$routeProvider', function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl:'templates/home.html',
                controller:'myapp.mainCtrl'
            })
            .when('/login', {
                templateUrl:'templates/login.html',
                controller:'myapp.loginCtrl'
            })
            .when('/about', {
                templateUrl:'templates/about.html',
                controller:'myapp.aboutCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });

            // $httpProvider.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
    }])

//Main Controller
    .controller('myapp.mainCtrl', ['$scope', '$http', function($scope, $http) {
      $scope.title = 'Simple Organizer';
      $scope.team = 'SP Lutsk';

      $http.get('js/user.json').then(function(response) {
          $scope.users = response.data;
        });

      var date = new Date();    // Date
      $scope.today = date;

    }]);

// --myapp.login--
angular.module('myapp.login', [])

//Auth factory
    .service('Auth', function($http) {

        this.login = function () {
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

                $http(req).then(function (response) {
                    var tokenUsers = response.data;
                    var serialResp = JSON.stringify(tokenUsers.token);
                    localStorage.setItem('user-token', serialResp);

                    var serialResp1 = JSON.stringify(tokenUsers.email);
                    localStorage.setItem('user-email', serialResp1);

                });
        };

        this.logout = function() {
            localStorage.removeItem('user-token')
            localStorage.removeItem('user-email')
            // localStorage.clear();
            // var returnResp = JSON.parse(localStorage.getItem('user-token'))
        };
    })

    //Login Controller
    .controller('myapp.loginCtrl', ['$scope', 'Auth', function($scope, Auth) {

        $scope.title = 'Login';
        $scope.logIn = Auth.login();
        $scope.logOut = Auth.logout();
        $scope.user = localStorage.getItem('user-email');
    }]);

// --myapp.about--
angular.module('myapp.about', [])

//About Controller
    .controller('myapp.aboutCtrl', ['$scope', function($scope) {

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
