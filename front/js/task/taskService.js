(function() {
    'use strict';

    angular
        .module('task')
        .service('ShortTaskByIdService', ShortTaskByIdService)
        .service('TaskByIdService', TaskByIdService)
        .service('EventByIdService', EventByIdService)
        .service('CategoryTaskByIdService', CategoryTaskByIdService);

    function ShortTaskByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/task/short-create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/task/short-list/')
                        .then(function(response){
                            console.log('Created shortTask & update ShortTaskList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/task/short-' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/task/short-list/')
                        .then(function(response){
                            console.log('Updated shortTask & update ShortTaskList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/task/short-' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/task/short-list/')
                        .then(function(response){
                            console.log('Deleted shortTask & update ShortTaskList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }
    function TaskByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/task/create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/task/list/')
                        .then(function(response){
                            console.log('Created task & update TaskList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/task/' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/task/list/')
                        .then(function(response){
                            console.log('Updated task & update TaskList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/task/' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/task/list/')
                        .then(function(response){
                            console.log('Deleted task & update TaskList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }
    function EventByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/task/event-create', data)
                .then(function() {
                    return $http.get('http://localhost:8000/task/event-list')
                        .then(function(response){
                            console.log('Created event & update EventList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/task/event-' + id, data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/task/event-list')
                        .then(function(response){
                            console.log('Updated event & update EventList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/task/event-' + id)
                .then(function() {
                    return $http.get('http://localhost:8000/task/event-list')
                        .then(function(response){
                            console.log('Deleted event & update EventList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }
    function CategoryTaskByIdService($http) {
        return {
            post: function(data) {
                return $http.post('http://localhost:8000/task/category-create/', data)
                .then(function() {
                    return $http.get('http://localhost:8000/task/category-list/')
                        .then(function(response){
                            console.log('Created category & update CategoryList OK!')
                            return response.data.results
                        })
                })
            },
            patch: function(id, data) {
                return $http.patch('http://localhost:8000/task/category-' + id + '/', data)
                .then(function(response) {
                    return $http.get('http://localhost:8000/task/category-list/')
                        .then(function(response){
                            console.log('Updated category & update CategoryList OK!')
                            return response.data.results
                        })
                })
            },
            delete: function(id) {
                return $http.delete('http://localhost:8000/task/category-' + id + '/')
                .then(function() {
                    return $http.get('http://localhost:8000/task/category-list/')
                        .then(function(response){
                            console.log('Deleted category & update CategoryList OK!')
                            return response.data.results
                        })
                })
            }
        }
    }

})();