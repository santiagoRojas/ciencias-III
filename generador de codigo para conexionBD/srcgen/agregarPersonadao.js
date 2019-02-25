'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarPersonadaoCtrl
 * @description
 * # AgregarPersonadaoCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarPersonadaoCtrl', function ($scope, $http) {
    $scope.title = 'Personadao';
    $scope.message = 'Agregar Personadao';

      $http.get(api_path + 'consultar?limit=0')
      .then(function(response) {
        $scope.consultar = response.data;
      });
      $http.get(api_path + 'eliminar?limit=0')
      .then(function(response) {
        $scope.eliminar = response.data;
      });

    $scope.add = function(){
      if($scope.Personadao.consultar == null){
        return;
      }
      if($scope.Personadao.eliminar == null){
        return;
      }
    var data = {
        consultar: $scope.Personadao.consultar,
        eliminar: $scope.Personadao.eliminar,
    };
    $http.post(api_path + 'Personadao',data);
    window.location.href = '#/Personadao';
  };

  $scope.cancel = function(){
    window.location.href = '#/Personadao';
  };
  });