(function(){
    'use strict';

    angular
        .module('invoice')
        .factory('InvoiceListFactory', InvoiceListFactory)
        .factory('InvoiceByIdFactory', InvoiceByIdFactory)
        .factory('BudgetAccountListFactory', BudgetAccountListFactory)
        .factory('BudgetAccountByIdFactory', BudgetAccountByIdFactory)
        .factory('BudgetCategoryListFactory', BudgetCategoryListFactory)
        .factory('BudgetCategoryByIdFactory', BudgetCategoryByIdFactory)
        .factory('CurrencyListFactory', CurrencyListFactory)
        .factory('CurrencyByIdFactory', CurrencyByIdFactory);

    function InvoiceListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/budget/invoice-list/')
                .then(function(response){
                    console.log('Get Invoice List OK!')
                    return response.data.results
                })
            }
        }
    }
    function InvoiceByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/budget/invoice-' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function BudgetAccountListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/budget/account-list/')
                .then(function(response){
                    console.log('Get BudgetAccount List OK!')
                    return response.data.results
                })
            }
        }
    }
    function BudgetAccountByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/budget/account-' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function BudgetCategoryListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/budget/category-list/')
                .then(function(response){
                    console.log('Get BudgetCategory List OK!')
                    return response.data.results
                })
            }
        }
    }
    function BudgetCategoryByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/budget/category-' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function CurrencyListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/budget/currency-list/')
                .then(function(response){
                    console.log('Get Currency List OK!')
                    return response.data.results
                })
            }
        }
    }
    function CurrencyByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/budget/currency-' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }

})();