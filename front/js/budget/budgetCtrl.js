(function() {
    'use strict';

    angular
        .module('budget')
        .controller('budgetCtrl', budgetCtrl);

    function budgetCtrl($scope, $http, InvoiceListFactory, InvoiceByIdService, BudgetAccountListFactory,
                        BudgetAccountByIdService, BudgetCategoryListFactory, BudgetCategoryByIdService,
                        CurrencyListFactory, CurrencyByIdService,) {

        initCtrl();

        function initCtrl(){
            InvoiceListFactory.get().then(function(resp) {
                $scope.listInv = resp;
            });
            BudgetAccountListFactory.get().then(function(resp) {
                $scope.listBA = resp;
            });
            BudgetCategoryListFactory.get().then(function(resp) {
                $scope.listBC = resp;
            });
            CurrencyListFactory.get().then(function(resp) {
                $scope.listC = resp;
            });

        };

        this.title = 'Budget'

        $scope.editItemState = false;
        $scope.addItemState = false;
        $scope.edit_status = '';

        $scope.invoice = {              //Invoice
            currency: '',
            amount: '',
            transaction_type: '',
            category: '',
            description: '',
            budget_account: ''
        };
        $scope.listInvoice = function() {
            InvoiceListFactory.get().then(function(resp) {
                $scope.listInv = resp;
            });
        };
        $scope.addInvoice = function() {
            $scope.addItemState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editInvoice = function(invoice) {
            $scope.invoice = invoice;
            $scope.editItemState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createInvoice = function() {
            $scope.addItemState = false;
            InvoiceByIdService.post($scope.invoice).then(function(resp) {
                $scope.listInv = resp;
            });
            $scope.invoice = {
                currency: '',
                amount: '',
                transaction_type: '',
                category: '',
                description: '',
                budget_account: ''
            };
        };
        $scope.updateInvoice = function() {
            $scope.editItemState = false;
            InvoiceByIdService.patch($scope.invoice.id, $scope.invoice).then(function(resp) {
                $scope.listInv = resp;
            });
            $scope.invoice = {
                currency: '',
                amount: '',
                transaction_type: '',
                category: '',
                description: '',
                budget_account: ''
            };
        };
        $scope.deleteInvoice = function(id) {
            InvoiceByIdService.delete(id).then(function(resp) {
                $scope.listInv = resp;
            });
        };
        $scope.budgetAccount = {              //Budget-Account
            currency: '',
            amount: '',
            name: '',
            short_name: '',
            description: ''
        };
        $scope.listBudgetAccount = function() {
            BudgetAccountListFactory.get().then(function(resp) {
                $scope.listBA = resp;
            });
        };
        $scope.addBudgetAccount = function() {
            $scope.addItemState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editBudgetAccount = function(budgetAccount) {
            $scope.budgetAccount = budgetAccount;
            $scope.editItemState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createBudgetAccount = function() {
            $scope.addItemState = false;
            BudgetAccountByIdService.post($scope.budgetAccount).then(function(resp) {
                $scope.listBA = resp;
            });
            $scope.budgetAccount = {
                currency: '',
                amount: '',
                name: '',
                short_name: '',
                description: ''
            };
        };
        $scope.updateBudgetAccount = function() {
            $scope.editItemState = false;
            BudgetAccountByIdService.patch($scope.budgetAccount.id, $scope.budgetAccount).then(function(resp) {
                $scope.listBA = resp;
            });
            $scope.budgetAccount = {
                currency: '',
                amount: '',
                name: '',
                short_name: '',
                description: ''
            };
        };
        $scope.deleteBudgetAccount = function(id) {
            BudgetAccountByIdService.delete(id).then(function(resp) {
                $scope.listBA = resp;
            });
        };
        $scope.budgetCategory = {title: ''};                //Budget-Category
        $scope.listBudgetCategory = function() {
            BudgetCategoryListFactory.get().then(function(resp) {
                $scope.listBC = resp;
            });
        };
        $scope.addBudgetCategory = function() {
            $scope.addItemState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editBudgetCategory = function(budgetCategory) {
            $scope.budgetCategory = budgetCategory;
            $scope.editItemState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createBudgetCategory = function() {
            $scope.addItemState = false;
            BudgetCategoryByIdService.post($scope.budgetCategory).then(function(resp) {
                $scope.listBC = resp;
            });
            $scope.budgetCategory = {title: ''};
        };
        $scope.updateBudgetCategory = function() {
            $scope.editItemState = false;
            BudgetCategoryByIdService.patch($scope.budgetCategory.id, $scope.budgetCategory).then(function(resp) {
                $scope.listBC = resp;
            });
            $scope.budgetCategory = {title: ''};
        };
        $scope.deleteBudgetCategory = function(id) {
            BudgetCategoryByIdService.delete(id).then(function(resp) {
                $scope.listBC = resp;
            });
        };
        $scope.currency = {                   //Currency
            name: '',
            short_name: ''
            };
        $scope.listCurrency = function() {
            CurrencyListFactory.get().then(function(resp) {
                $scope.listC = resp;
            });
        };
        $scope.addCurrency = function() {
            $scope.addItemState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editCurrency = function(currency) {
            $scope.currency = currency;
            $scope.editItemState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createCurrency = function() {
            $scope.addItemState = false;
            CurrencyByIdService.post($scope.currency).then(function(resp) {
                $scope.listC = resp;
            });
            $scope.currency = {
                name: '',
                short_name: ''
                };
        };
        $scope.updateCurrency = function() {
            $scope.editItemState = false;
            CurrencyByIdService.patch($scope.currency.id, $scope.currency).then(function(resp) {
                $scope.listC = resp;
            });
            $scope.currency = {
                name: '',
                short_name: ''
                };
        };
        $scope.deleteCurrency = function(id) {
            CurrencyByIdService.delete(id).then(function(resp) {
                $scope.listC = resp;
            });
        };

    }
})();