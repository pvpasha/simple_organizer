(function(){
    'use strict';

    angular
        .module('diary')
        .factory('DiaryListFactory', DiaryListFactory)
        .factory('DiaryByIdFactory', DiaryByIdFactory);

    function DiaryListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/diary/list/')
                .then(function(response){
                    console.log('Get Diary List OK!')
                    return response.data.results
                })
            }
        }
    }
    function DiaryByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/diary/' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }

})();