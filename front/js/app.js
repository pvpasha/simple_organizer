(function(){
    'use strict';

// declare modules
angular.module('Home', []);
angular.module('Login', []);
angular.module('About', []);
angular.module('Route', []);


angular
    .module('app', [
        'Home',
        'Login',
        'About',
        'Route'
     ])

})();