(function(){
    'use strict';

// declare modules
angular.module('accounts', ['ngStorage']);
angular.module('budget', []);
angular.module('contacts', []);
angular.module('diary', []);
angular.module('password', []);
angular.module('task', []);

angular
    .module('app', [
        'accounts',
        'budget',
        'contacts',
        'diary',
        'password',
        'task',
        'route'
        ])
})();