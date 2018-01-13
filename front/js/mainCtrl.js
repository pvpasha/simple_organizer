var app = angular.module("myApp", ["ngRoute"]);

app.config(['$routeProvider', function($routeProvider){
    $routeProvider
        .when('/', {
            templateUrl:'templates/home.html',
            controller:'homeCtrl'
        })
        .when('/login', {
            templateUrl:'templates/login.html',
            controller:'loginCtrl'
        })
        .when('/about', {
            templateUrl:'templates/about.html',
            controller:'aboutCtrl'
        })
        .otherwise({
            redirectTo: '/'
        });

}]);

//Main Controller
app.controller('mainCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
  $scope.title = 'Simple Organizer';
  $scope.team = 'SP Lutsk';

  $http.get('js/user.json').then(function(response) {
      $scope.users = response.data;
    });

  var date = new Date();
  $scope.today = date;

}]);

//Home Controller
app.controller('homeCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.title = 'Home';

}]);

//Login Controller
app.controller('loginCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.title = 'Login';

}]);

//About Controller
app.controller('aboutCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.title = 'About';

}]);


