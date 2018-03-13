(function() {
    'use strict';

    angular
        .module('budget')
        .controller('budgetCtrl', budgetCtrl)
        .controller('invoiceCtrl', invoiceCtrl)
        .controller('budgetAcCtrl', budgetAcCtrl)
        .controller('budgetCatCtrl', budgetCatCtrl)
        .controller('currencyCtrl', currencyCtrl);

    function budgetCtrl($scope, $http, TotalAmountFactory, TotalAmountByBAListFactory) {

        initCtrl();

        function initCtrl(){
            TotalAmountFactory.get().then(function(resp) {
                $scope.totalAmountValue = resp;
            });
            TotalAmountByBAListFactory.get().then(function(resp) {
                $scope.totalAmountBAValue = resp;
            });
        };

        this.title = 'Budget'

        $scope.editItemState = false;
        $scope.addItemState = false;
        $scope.edit_status = '';

        $scope.totalAmountByBAList = function() {
            TotalAmountByBAListFactory.get().then(function(resp) {
                $scope.totalAmountBAValue = resp;
            });
        };
        $scope.totalAmount = function() {
            TotalAmountFactory.get().then(function(resp) {
                $scope.totalAmountValue = resp;
            });
        };
    }
    function invoiceCtrl($scope, $http, InvoiceListFactory, InvoiceByIdService) {

        initCtrl();

        function initCtrl(){
            InvoiceListFactory.get().then(function(resp) {
                $scope.listInv = resp;
            });
        };

        this.title = 'Invoice'

        $scope.editItemState = false;
        $scope.addItemState = false;
        $scope.edit_status = '';

        $scope.invoice = {
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
        $scope.cancel = function() {
            $scope.editItemState = false
            $scope.addItemState = false
            $scope.invoice = {
                currency: '',
                amount: '',
                transaction_type: '',
                category: '',
                description: '',
                budget_account: ''
            };
        };
    }
    function budgetAcCtrl($scope, $http, BudgetAccountListFactory, BudgetAccountByIdService) {

        initCtrl();

        function initCtrl(){
            BudgetAccountListFactory.get().then(function(resp) {
                $scope.listBA = resp;
            });
        };

        this.title = 'Budget Account'

        $scope.editItemState = false;
        $scope.addItemState = false;
        $scope.edit_status = '';

        $scope.budgetAccount = {
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
        $scope.cancel = function() {
            $scope.editItemState = false
            $scope.addItemState = false
            $scope.budgetAccount = {
                currency: '',
                amount: '',
                name: '',
                short_name: '',
                description: ''
            };
        };
    }
    function budgetCatCtrl($scope, $http, BudgetCategoryListFactory, BudgetCategoryByIdService) {

        initCtrl();

        function initCtrl(){
            BudgetCategoryListFactory.get().then(function(resp) {
                $scope.listBC = resp;
            });
        };

        this.title = 'Budget Category'

        $scope.editItemState = false;
        $scope.addItemState = false;
        $scope.edit_status = '';

        $scope.budgetCategory = {title: ''};
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
        $scope.cancel = function() {
            $scope.editItemState = false
            $scope.addItemState = false
            $scope.budgetCategory = {title: ''};
        };
    }
    function currencyCtrl($scope, $http, CurrencyListFactory, CurrencyByIdService) {

        initCtrl();

        function initCtrl(){
            CurrencyListFactory.get().then(function(resp) {
                $scope.listC = resp;
            });
        };

        this.title = 'Currency'

        $scope.editItemState = false;
        $scope.addItemState = false;
        $scope.edit_status = '';

        $scope.currency = {
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
        $scope.cancel = function() {
            $scope.editItemState = false
            $scope.addItemState = false
            $scope.currency = {
                name: '',
                short_name: ''
                };
        };

    }
})();