(function() {
    'use strict';

    angular
        .module('budget')
        .service('InvoiceByIdService', InvoiceByIdService)
        .service('BudgetAccountByIdService', BudgetAccountByIdService)
        .service('BudgetCategoryByIdService', BudgetCategoryByIdService)
        .service('CurrencyByIdService', CurrencyByIdService);

    function InvoiceByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/budget/invoice-create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/budget/invoice-list/')
                        .then(function(response){
                            console.log('Created invoice & update InvoiceList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/budget/invoice-' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/budget/invoice-list/')
                        .then(function(response){
                            console.log('Updated invoice & update InvoiceList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/budget/invoice-' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/budget/invoice-list/')
                        .then(function(response){
                            console.log('Deleted invoice & update InvoiceList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }
    function BudgetAccountByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/budget/account-create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/budget/account-list/')
                        .then(function(response){
                            console.log('Created account & update BudgetAccountList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/budget/account-' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/budget/account-list/')
                        .then(function(response){
                            console.log('Updated account & update BudgetAccountList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/budget/account-' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/budget/account-list/')
                        .then(function(response){
                            console.log('Deleted account & update BudgetAccountList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }
    function BudgetCategoryByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/budget/category-create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/budget/category-list/')
                        .then(function(response){
                            console.log('Created category & update BudgetCategoryList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/budget/category-' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/budget/category-list/')
                        .then(function(response){
                            console.log('Updated category & update BudgetCategoryList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/budget/category-' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/budget/category-list')
                        .then(function(response){
                            console.log('Deleted category & update BudgetCategoryList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }
    function CurrencyByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/budget/currency-create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/budget/currency-list/')
                        .then(function(response){
                            console.log('Created currency & update CurrencyList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/budget/currency-' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/budget/currency-list/')
                        .then(function(response){
                            console.log('Updated currency & update CurrencyList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/budget/currency-' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/budget/currency-list')
                        .then(function(response){
                            console.log('Deleted currency & update CurrencyList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }

})();