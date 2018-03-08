(function() {
    'use strict';

    angular
        .module('task')
        .controller('taskCtrl', taskCtrl);

    function taskCtrl($scope, $http, ShortTaskListFactory, ShortTaskByIdService, TaskListFactory, TaskByIdService,
                        EventListFactory, EventByIdService, CategoryTaskListFactory, CategoryTaskByIdService) {

        initCtrl();

        function initCtrl(){
            ShortTaskListFactory.get().then(function(resp) {
                $scope.listST = resp;
            });
            TaskListFactory.get().then(function(resp) {
                $scope.listT = resp;
            });
            EventListFactory.get().then(function(resp) {
                $scope.listE = resp;
            });
            CategoryTaskListFactory.get().then(function(resp) {
                $scope.listCT = resp;
            });
        };

        this.title = 'Task'

        $scope.editTaskState = false;
        $scope.addTaskState = false;
        $scope.edit_status = '';

        $scope.shortTask = {                    //ShortTask
            title: '',
            body: '',
            finished: ''
        };
        $scope.listShortTask = function() {
            ShortTaskListFactory.get().then(function(resp) {
                $scope.listST = resp;
            });
        };
        $scope.addShortTask= function() {
            $scope.addTaskState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editShortTask = function(shortTask) {
            $scope.shortTask = shortTask;
            $scope.editTaskState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createShortTask = function() {
            $scope.addTaskState = false;
            ShortTaskByIdService.post($scope.shortTask).then(function(resp) {
                $scope.listST = resp;
            });
            $scope.shortTask = {
                title: '',
                body: '',
                finished: ''
            };
        };
        $scope.updateShortTask = function() {
            $scope.editTaskState = false;
            ShortTaskByIdService.patch($scope.shortTask.id, $scope.shortTask).then(function(resp) {
                $scope.listST = resp;
            });
            $scope.shortTask = {
                title: '',
                body: '',
                finished: ''
            };
        };
        $scope.deleteShortTask = function(id) {
            ShortTaskByIdService.delete(id).then(function(resp) {
                $scope.listST = resp;
            });
        };
        $scope.task = {                    //Task
            title: '',
            body: '',
            category: '',
            starting_date: '',
            finishing_date: '',
            finished: '',
            reminder_date: ''
        };
        $scope.listTask = function() {
            TaskListFactory.get().then(function(resp) {
                $scope.listT = resp;
            });
        };
        $scope.addTask= function() {
            $scope.addTaskState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editTask = function(task) {
            $scope.task = task;
            $scope.editTaskState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createTask = function() {
            $scope.addTaskState = false;
            TaskByIdService.post($scope.task).then(function(resp) {
                $scope.listT = resp;
            });
            $scope.task = {
                title: '',
                body: '',
                category: '',
                starting_date: '',
                finishing_date: '',
                finished: '',
                reminder_date: ''
            };
        };
        $scope.updateTask = function() {
            $scope.editTaskState = false;
            TaskByIdService.patch($scope.task.id, $scope.task).then(function(resp) {
                $scope.listT = resp;
            });
            $scope.task = {
                title: '',
                body: '',
                category: '',
                starting_date: '',
                finishing_date: '',
                finished: '',
                reminder_date: ''
            };
        };
        $scope.deleteTask = function(id) {
            TaskByIdService.delete(id).then(function(resp) {
                $scope.listS = resp;
            });
        };
        $scope.event = {                    //Event
            title: '',
            body: '',
            event_date_start: '',
            event_date_finish: '',
            reminder_date: ''
        };
        $scope.listEvent = function() {
            EventListFactory.get().then(function(resp) {
                $scope.listE = resp;
            });
        };
        $scope.addEvent= function() {
            $scope.addTaskState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editEvent = function(event) {
            $scope.event = event;
            $scope.editTaskState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createEvent = function() {
            $scope.addTaskState = false;
            EventByIdService.post($scope.event).then(function(resp) {
                $scope.listE = resp;
            });
            $scope.event = {
                title: '',
                body: '',
                event_date_start: '',
                event_date_finish: '',
                reminder_date: ''
            };
        };
        $scope.updateEvent = function() {
            $scope.editTaskState = false;
            EventByIdService.patch($scope.event.id, $scope.event).then(function(resp) {
                $scope.listE = resp;
            });
            $scope.event = {
                title: '',
                body: '',
                event_date_start: '',
                event_date_finish: '',
                reminder_date: ''
            };
        };
        $scope.deleteEvent = function(id) {
            EventByIdService.delete(id).then(function(resp) {
                $scope.listE = resp;
            });
        };
        $scope.categoryTask = {title: ''};          //Category
        $scope.listCategoryTask = function() {
            CategoryTaskListFactory.get().then(function(resp) {
                $scope.listCT = resp;
            });
        };
        $scope.addCategoryTask= function() {
            $scope.addTaskState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editCategoryTask = function(categoryTask) {
            $scope.categoryTask = categoryTask;
            $scope.editTaskState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createCategoryTask = function() {
            $scope.addTaskState = false;
            CategoryTaskByIdService.post($scope.categoryTask).then(function(resp) {
                $scope.listCT = resp;
            });
            $scope.categoryTask = {title: ''};
        };
        $scope.updateCategoryTask = function() {
            $scope.editTaskState = false;
            CategoryTaskByIdService.patch($scope.categoryTask.id, $scope.categoryTask).then(function(resp) {
                $scope.listCT = resp;
            });
            $scope.categoryTask = {title: ''};
        };
        $scope.deleteCategoryTask = function(id) {
            CategoryTaskByIdService.delete(id).then(function(resp) {
                $scope.listCT = resp;
            });
        };

    }
})();