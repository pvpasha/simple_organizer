(function() {
    'use strict';

    angular
        .module('budget')
        .filter('transactionTypeIcon', transactionTypeIcon)
        .filter('transactionTypeText', transactionTypeText);

    function transactionTypeIcon(){
        return function(data) {
            if (data == 1) { return 'glyphicon glyphicon-log-in'
            } else { return 'glyphicon glyphicon-log-out'
            }
        }
    }
    function transactionTypeText(){
        return function(data) {
            if (data == 1) { return 'Income'
            } else { return 'Outcome'
            }
        }
    }

})();