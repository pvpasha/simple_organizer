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
    function invoiceCtrl($scope, $http, InvoiceListFactory, InvoiceByIdService, CurrencyListFactory,
                            BudgetAccountListFactory, BudgetCategoryListFactory) {

        initCtrl();

        function initCtrl(){
            InvoiceListFactory.get().then(function(response) {
                $scope.listInvoice = response;
            });
        };

        this.title = 'Invoice'

        $scope.editItemState = false;
        $scope.addItemState = false;
        $scope.edit_status = '';

        $scope.invoice = {
            currency: '',
            amount: 0,
            transaction_type: '',
            category: null,
            description: '',
            budget_account: ''
        };
        $scope.listInvoice = function() {
            InvoiceListFactory.get().then(function(resp) {
                $scope.listInvoice = resp;
            });
        };
        $scope.addInvoice = function() {
            $scope.addItemState = true;
            $scope.edit_status = 'Add Form';
            CurrencyListFactory.get().then(function(currency) {
                $scope.listCurrency = currency;
            });
            BudgetAccountListFactory.get().then(function(account) {
                $scope.listBudgetAccount = account;
            });
            BudgetCategoryListFactory.get().then(function(category) {
                $scope.listBudgetCategory = category;
            });
        };
        $scope.editInvoice = function(invoice) {
            $scope.invoice = invoice;
            $scope.editItemState = true;
            $scope.edit_status = 'Edit Form';
            CurrencyListFactory.get().then(function(currency) {
                $scope.listCurrency = currency;
            });
            BudgetAccountListFactory.get().then(function(account) {
                $scope.listBudgetAccount = account;
            });
            BudgetCategoryListFactory.get().then(function(category) {
                $scope.listBudgetCategory = category;
            });
        };
        $scope.createInvoice = function() {
            $scope.addItemState = false;
            var a = document.getElementById('selected_currency');
            var currency_id = a.options[a.selectedIndex].value;
            $scope.invoice.currency = currency_id;
            var b = document.getElementById('selected_transaction_type');
            var transaction_type_id = b.options[b.selectedIndex].value;
            $scope.invoice.transaction_type = transaction_type_id;
            var c = document.getElementById('selected_budget_account');
            var budget_account_id = c.options[c.selectedIndex].value;
            $scope.invoice.budget_account = budget_account_id;
            var d = document.getElementById('selected_category');
            var category_id = d.options[d.selectedIndex].value;
            $scope.invoice.category = category_id;
            InvoiceByIdService.post($scope.invoice).then(function(response) {
                $scope.listInvoice = response;
            });
            $scope.invoice = {
                currency: '',
                amount: 0,
                transaction_type: '',
                category: null,
                description: '',
                budget_account: ''
            };
        };
        $scope.updateInvoice = function() {
            $scope.editItemState = false;
            InvoiceByIdService.patch($scope.invoice.id, $scope.invoice).then(function(response) {
                $scope.listInvoice = response;
            });
            $scope.invoice = {
                currency: '',
                amount: 0,
                transaction_type: '',
                category: null,
                description: '',
                budget_account: ''
            };
        };
        $scope.deleteInvoice = function(id) {
            InvoiceByIdService.delete(id).then(function(response) {
                $scope.listInvoice = response;
            });
        };
        $scope.cancel = function() {
            $scope.editItemState = false
            $scope.addItemState = false
            $scope.invoice = {
                currency: '',
                amount: 0,
                transaction_type: '',
                category: null,
                description: '',
                budget_account: ''
            };
        };
    }
    function budgetAcCtrl($scope, $http, BudgetAccountListFactory, BudgetAccountByIdService, CurrencyListFactory) {

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
            amount: 0,
            name: '',
            short_name: '',
            description: null
        };
        $scope.listBudgetAccount = function() {
            BudgetAccountListFactory.get().then(function(resp) {
                $scope.listBA = resp;
            });
        };
        $scope.addBudgetAccount = function() {
            $scope.addItemState = true;
            $scope.edit_status = 'Add Form';
            CurrencyListFactory.get().then(function(currency) {
                $scope.listCurrency = currency;
            });
        };
        $scope.editBudgetAccount = function(budgetAccount) {
            $scope.budgetAccount = budgetAccount;
            $scope.editItemState = true;
            $scope.edit_status = 'Edit Form';
            CurrencyListFactory.get().then(function(currency) {
                $scope.listCurrency = currency;
            });
        };
        $scope.createBudgetAccount = function() {
            $scope.addItemState = false;
            var e = document.getElementById('selected_currency');
            var currency_id = e.options[e.selectedIndex].value;
            $scope.budgetAccount.currency = currency_id;
            BudgetAccountByIdService.post($scope.budgetAccount).then(function(resp) {
                $scope.listBA = resp;
            });
            $scope.budgetAccount = {
                currency: '',
                amount: 0,
                name: '',
                short_name: '',
                description: null
            };
        };
        $scope.updateBudgetAccount = function() {
            $scope.editItemState = false;
            var e = document.getElementById('selected_currency');
            var currency_id = e.options[e.selectedIndex].value;
            $scope.budgetAccount.currency = currency_id;
            BudgetAccountByIdService.patch($scope.budgetAccount.id, $scope.budgetAccount).then(function(resp) {
                $scope.listBA = resp;
            });
            $scope.budgetAccount = {
                currency: '',
                amount: 0,
                name: '',
                short_name: '',
                description: null
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
                amount: 0,
                name: '',
                short_name: '',
                description: null
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