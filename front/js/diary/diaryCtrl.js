(function() {
    'use strict';

    angular
        .module('diary')
        .controller('diaryCtrl', diaryCtrl);

    function diaryCtrl($scope, $http, DiaryListFactory, DiaryByIdService) {

        initCtrl();

        function initCtrl(){
            DiaryListFactory.get().then(function(resp) {
                $scope.items = resp;
            });
        };

        this.title = 'Diary'

        $scope.editDiaryState = false;
        $scope.addDiaryState = false;
        $scope.edit_status = '';

        $scope.diary = {
            title: '',
            body: ''
        };
        $scope.listDiary = function() {
            DiaryListFactory.get().then(function(resp) {
                $scope.items = resp;
            });
        };
        $scope.addDiary = function() {
            $scope.addDiaryState = true;
            $scope.edit_status = 'Add Form';
        };
        $scope.editDiary = function(diary) {
            $scope.diary = diary;
            $scope.editDiaryState = true;
            $scope.edit_status = 'Edit Form';
        };
        $scope.createDiary = function() {
            $scope.addDiaryState = false;
            DiaryByIdService.post($scope.diary).then(function(resp) {
                $scope.items = resp;
            });
            $scope.diary = {
                title: '',
                body: ''
            };
        };
        $scope.updateDiary = function() {
            $scope.editDiaryState = false;
            DiaryByIdService.patch($scope.diary.id, $scope.diary).then(function(resp) {
                $scope.items = resp;
            });
            $scope.diary = {
                title: '',
                body: ''
            };
        };
        $scope.deleteDiary = function(id) {
            DiaryByIdService.delete(id).then(function(resp) {
                $scope.items = resp;
            });
        };

    }
})();