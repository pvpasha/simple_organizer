(function(){
    'use strict';

    angular
        .module('task')
        .factory('ShortTaskListFactory', ShortTaskListFactory)
        .factory('ShortTaskByIdFactory', ShortTaskByIdFactory)
        .factory('TaskListFactory', TaskListFactory)
        .factory('TaskByIdFactory', TaskByIdFactory)
        .factory('EventListFactory', EventListFactory)
        .factory('EventByIdFactory', EventByIdFactory)
        .factory('CategoryTaskListFactory', CategoryTaskListFactory)
        .factory('CategoryTaskByIdFactory', CategoryTaskByIdFactory);

    function ShortTaskListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/task/short-list/')
                .then(function(response){
                    console.log('Get ShortTask List OK!')
                    return response.data.results
                })
            }
        }
    }
    function ShortTaskByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/task/short-' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function TaskListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/task/task/list/')
                .then(function(response){
                    console.log('Get Task List OK!')
                    return response.data.results
                })
            }
        }
    }
    function TaskByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/task/task/' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function EventListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/task/event-list/')
                .then(function(response){
                    console.log('Get Event List OK!')
                    return response.data.results
                })
            }
        }
    }
    function EventByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/task/event-' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
    function CategoryTaskListFactory($http) {
        return {
            get: function() {
                return $http.get('http://localhost:8000/task/category-list/')
                .then(function(response){
                    console.log('Get CategoryTask List OK!')
                    return response.data.results
                })
            }
        }
    }
    function CategoryTaskByIdFactory($http) {
        return {
            get: function(id) {
                return $http.get('http://localhost:8000/task/category-' + id + '/')
                .then(function(response) {
                    return response.data
                })
            }
        }
    }
})();