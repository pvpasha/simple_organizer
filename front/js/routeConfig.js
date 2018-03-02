(function(){
    'use strict';

angular
    .module('route', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl:'templates/home.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .when('/sing-in', {
                templateUrl:'templates/accounts/sing-in.html',
                controller:'accountsCtrl',
                controllerAs: 'vm'
            })
            .when('/sing-up', {
                templateUrl:'templates/accounts/sing-up.html',
                controller:'accountsCtrl',
                controllerAs: 'vm'
            })
            .when('/logout', {
                templateUrl:'templates/accounts/logout.html',
                controller:'accountsCtrl',
                controllerAs: 'vm'
            })
            .when('/profile', {
                templateUrl:'templates/accounts/profile.html',
                controller:'accountsCtrl',
                controllerAs: 'vm'
            })
            .when('/budget', {
                templateUrl:'templates/budget/budget-home.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .when('/contacts', {
                templateUrl:'templates/contacts/contacts.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .when('/diary', {
                templateUrl:'templates/diary/diary.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .when('/password', {
                templateUrl:'templates/password/password.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .when('/task', {
                templateUrl:'templates/task/task-home.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .when('/about', {
                templateUrl:'templates/about.html',
                controller:'homeCtrl',
                controllerAs: 'vm'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);
})();