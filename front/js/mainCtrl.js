(function() {
    'use strict';

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
    .controller('myapp.mainCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
      $scope.title = 'Simple Organizer';
      $scope.team = 'SP Lutsk';

      $http.get('js/user.json').then(function(response) {
          $scope.users = response.data;
        });

      var date = new Date();    // Date
      $scope.today = date;

}]);

//Login Controller
angular.module('myapp.login', [])
    .controller('myapp.loginCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {

        $scope.title = 'Login';

        $scope.logIn = function() {
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

            $http(req).then(function(response){
                var tokenUsers = response.data
                var serialResp = JSON.stringify(tokenUsers.token);
                localStorage.setItem('users-token', serialResp);

                var serialResp = JSON.stringify(tokenUsers.email);
                localStorage.setItem('users-email', serialResp);

                $scope.token = localStorage.getItem('users-email');

    //            localStorage.removeItem('users-token')
    //            localStorage.clear();

                // var returnResp = JSON.parse(localStorage.getItem('user-token'))
            });
        };
}]);

//About Controller
angular.module('myapp.about', [])
    .controller('myapp.aboutCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {

        $scope.title = 'About';
}]);
//console.log(title);

angular.module('myapp', [
    'myapp.main',
    'myapp.login',
    'myapp.about'
]);

})();
