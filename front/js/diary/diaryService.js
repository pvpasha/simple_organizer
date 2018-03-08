(function() {
    'use strict';

    angular
        .module('diary')
        .service('DiaryByIdService', DiaryByIdService);

    function DiaryByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/diary/create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/diary/list/')
                        .then(function(response){
                            console.log('Created diary & update DiaryList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/diary/' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/diary/list/')
                        .then(function(response){
                            console.log('Updated diary & update DiaryList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/diary/' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/diary/list/')
                        .then(function(response){
                            console.log('Deleted diary & update DiaryList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }

})();