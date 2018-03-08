(function(){
    'use strict';

angular
    .module('route', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider){
        $routeProvider
            .when('/', {
                templateUrl:'templates/home.html',
                controller:'accountsCtrl',
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
                controller:'budgetCtrl',
                controllerAs: 'vm'
            })
            .when('/budget/invoice', {
                templateUrl:'templates/budget/invoice.html',
                controller:'invoiceCtrl',
                controllerAs: 'vm'
            })
            .when('/budget/account', {
                templateUrl:'templates/budget/budget-account.html',
                controller:'budgetAcCtrl',
                controllerAs: 'vm'
            })
            .when('/budget/currency', {
                templateUrl:'templates/budget/currency.html',
                controller:'currencyCtrl',
                controllerAs: 'vm'
            })
            .when('/budget/category', {
                templateUrl:'templates/budget/budget-category.html',
                controller:'budgetCatCtrl',
                controllerAs: 'vm'
            })
            .when('/contacts', {
                templateUrl:'templates/contacts/contacts.html',
                controller:'contactsCtrl',
                controllerAs: 'vm'
            })
            .when('/diary', {
                templateUrl:'templates/diary/diary.html',
                controller:'diaryCtrl',
                controllerAs: 'vm'
            })
            .when('/password', {
                templateUrl:'templates/password/password.html',
                controller:'passwordCtrl',
                controllerAs: 'vm'
            })
            .when('/task', {
                templateUrl:'templates/task/task.html',
                controller:'taskCtrl',
                controllerAs: 'vm'
            })
            .when('/task/short', {
                templateUrl:'templates/task/short-task.html',
                controller:'shortTaskCtrl',
                controllerAs: 'vm'
            })
            .when('/task/event', {
                templateUrl:'templates/task/event.html',
                controller:'eventCtrl',
                controllerAs: 'vm'
            })
            .when('/task/category', {
                templateUrl:'templates/task/category-task.html',
                controller:'catTaskCtrl',
                controllerAs: 'vm'
            })
            .when('/about', {
                templateUrl:'templates/about.html',
                controller:'accountsCtrl',
                controllerAs: 'vm'
            })
            .otherwise({
                redirectTo: '/'
            });
    }]);
})();