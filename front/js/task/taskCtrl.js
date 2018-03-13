(function() {
    'use strict';

    angular
        .module('task')
        .controller('shortTaskCtrl', shortTaskCtrl)
        .controller('taskCtrl', taskCtrl)
        .controller('eventCtrl', eventCtrl)
        .controller('catTaskCtrl', catTaskCtrl);

    function shortTaskCtrl($scope, $http, ShortTaskListFactory, ShortTaskByIdService) {

        initCtrl();

        function initCtrl(){
            ShortTaskListFactory.get().then(function(resp) {
                $scope.listST = resp;
            });
        };

        this.title = 'Short Task'

        $scope.editTaskState = false;
        $scope.addTaskState = false;
        $scope.edit_status = '';

        $scope.shortTask = {
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
        $scope.cancel = function() {
            $scope.editTaskState = false
            $scope.addTaskState = false
            $scope.shortTask = {
                title: '',
                body: '',
                finished: ''
            };
        };
    }
    function taskCtrl($scope, $http, TaskListFactory, TaskByIdService) {

        initCtrl();

        function initCtrl(){
            TaskListFactory.get().then(function(resp) {
                $scope.listT = resp;
            });
        };

        this.title = 'Task'

        $scope.editTaskState = false;
        $scope.addTaskState = false;
        $scope.edit_status = '';

        $scope.task = {
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
        };  // TODO: Make list CategoryForTask in add&&edit form
        $scope.listCategoryForTask = function() {
            CategoryTaskListFactory.get().then(function(resp) {
                $scope.listCatForTask = resp;
            });
        };
        $scope.addTask= function() {
            $scope.addTaskState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editTask = function(task) {
            var starting_date = new Date(task.starting_date);
            var finishing_date = new Date(task.finishing_date);
            var reminder_date = new Date(task.reminder_date);
            $scope.task = task;
            $scope.task.starting_date = starting_date;
            $scope.task.finishing_date = finishing_date;
            $scope.task.reminder_date = reminder_date;
            $scope.editTaskState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.updateTask = function() {
            $scope.editTaskState = false;
            var starting_date = $scope.task.starting_date.toISOString();
            var finishing_date = $scope.task.finishing_date.toISOString();
            var reminder_date = $scope.task.reminder_date.toISOString();
            $scope.task.starting_date = starting_date;
            $scope.task.finishing_date = finishing_date;
            $scope.task.reminder_date = reminder_date;
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
        $scope.createTask = function() {
            $scope.addTaskState = false;
            var starting_date2 = $scope.task.starting_date.toISOString();
            var finishing_date2 = $scope.task.finishing_date.toISOString();
            var reminder_date2 = $scope.task.reminder_date.toISOString();
            $scope.task.starting_date = starting_date2;
            $scope.task.finishing_date = finishing_date2;
            $scope.task.reminder_date = reminder_date2;
            console.log($scope.task)
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
        $scope.deleteTask = function(id) {
            TaskByIdService.delete(id).then(function(resp) {
                $scope.listS = resp;
            });
        };
        $scope.cancel = function() {
            $scope.editTaskState = false
            $scope.addTaskState = false
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
    }
    function eventCtrl($scope, $http, EventListFactory, EventByIdService) {

        initCtrl();

        function initCtrl(){
            EventListFactory.get().then(function(resp) {
                $scope.listE = resp;
            });
        };

        this.title = 'Event'

        $scope.editTaskState = false;
        $scope.addTaskState = false;
        $scope.edit_status = '';

        $scope.event = {
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
            $scope.editTaskState = true;
            $scope.edit_status = 'Edit Form';
            var event_date_start = new Date(event.event_date_start);
            var event_date_finish = new Date(event.event_date_finish);
            var reminder_date = new Date(event.reminder_date);
            $scope.event = event;
            $scope.event.event_date_start = event_date_start;
            $scope.event.event_date_finish = event_date_finish;
            $scope.event.reminder_date = reminder_date;
        };
        $scope.createEvent = function() {
            $scope.addTaskState = false;
            var event_date_start2 = $scope.event.event_date_start.toISOString();
            var event_date_finish2 = $scope.event.event_date_finish.toISOString();
            var reminder_date2 = $scope.event.reminder_date.toISOString();
            $scope.event.event_date_start = event_date_start2;
            $scope.event.event_date_finish = event_date_finish2;
            $scope.event.reminder_date = reminder_date2;
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
            var event_date_start2 = $scope.event.event_date_start.toISOString();
            var event_date_finish2 = $scope.event.event_date_finish.toISOString();
            var reminder_date2 = $scope.event.reminder_date.toISOString();
            $scope.event.event_date_start = event_date_start2;
            $scope.event.event_date_finish = event_date_finish2;
            $scope.event.reminder_date = reminder_date2;
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
        $scope.cancel = function() {
            $scope.editTaskState = false
            $scope.addTaskState = false
            $scope.event = {
                title: '',
                body: '',
                event_date_start: '',
                event_date_finish: '',
                reminder_date: ''
            };
        };
    }
    function catTaskCtrl($scope, $http, CategoryTaskListFactory, CategoryTaskByIdService) {

        initCtrl();

        function initCtrl(){
            CategoryTaskListFactory.get().then(function(resp) {
                $scope.listCT = resp;
            });
        };

        this.title = 'Category Task'

        $scope.editTaskState = false;
        $scope.addTaskState = false;
        $scope.edit_status = '';

        $scope.categoryTask = {title: ''};
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
        $scope.cancel = function() {
            $scope.editTaskState = false
            $scope.addTaskState = false
            $scope.categoryTask = {title: ''};
        };
    }
})();