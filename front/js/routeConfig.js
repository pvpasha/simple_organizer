(function(){
    'use strict';

angular
    .module('Route', ['ngRoute'])

    /* routes configs */
    .config(['$routeProvider', function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl:'templates/home.html',
                controller:'homeCtrl',
                controllerAs: 'home'
            })
            .when('/login', {
                templateUrl:'templates/login.html',
                controller:'loginCtrl',
                controllerAs: 'login'
            })
            .when('/about', {
                templateUrl:'templates/about.html',
                controller:'aboutCtrl',
                controllerAs: 'about'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);

})();