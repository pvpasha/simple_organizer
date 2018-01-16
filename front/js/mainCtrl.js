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

  var date = new Date();    // Date
  $scope.today = date;

}]);

//Home Controller
app.controller('homeCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.title = 'Home';

}]);

//Login Controller
app.controller('loginCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.title = 'Login';

    $scope.logIn = function() {

        var data = ({
        email: $scope.email,
        password: $scope.password
        });

//        var config = {
//            headers : { 'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'}
//        }

        $http.post('http://localhost:8000/accounts/api-login/', data)
            .success(function (result) {
                console.log('Success!');
            })
            .error(function (result) {
                console.log('Error');
            });

    };

    //$http.post('/accounts/api-login/', data).then(function(response) {
    //      $scope.users = response.data;

}]);

//About Controller
app.controller('aboutCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $scope.title = 'About';

}]);

//console.log(name);


