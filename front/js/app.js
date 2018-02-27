(function(){
    'use strict';

// declare modules
angular.module('home', []);
angular.module('accounts', ['ngStorage']);

angular
    .module('app', [
        'home',
        'accounts',
        'route'
     ])

})();