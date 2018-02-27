(function(){
    'use strict';

angular
    .module('route', ['ngRoute'])

    /* routes configs */
    .config(['$routeProvider', function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl:'templates/home.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .when('/login', {
                templateUrl:'templates/accounts/login.html',
                controller:'accountsCtrl',
                controllerAs: 'vm'
            })
//            .when('/about', {
//                templateUrl:'templates/about.html',
//                controller:'aboutCtrl',
//                controllerAs: 'vm'
//            })
            .otherwise({
                redirectTo: '/'
            });
    }]);

})();