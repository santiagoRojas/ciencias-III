'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarCajerodaoCtrl
 * @description
 * # AgregarCajerodaoCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarCajerodaoCtrl', function ($scope, $http) {
    $scope.title = 'Cajerodao';
    $scope.message = 'Agregar Cajerodao';

      $http.get(api_path + 'consultar?limit=0')
      .then(function(response) {
        $scope.consultar = response.data;
      });
      $http.get(api_path + 'eliminar?limit=0')
      .then(function(response) {
        $scope.eliminar = response.data;
      });

    $scope.add = function(){
      if($scope.Cajerodao.consultar == null){
        return;
      }
      if($scope.Cajerodao.eliminar == null){
        return;
      }
    var data = {
        consultar: $scope.Cajerodao.consultar,
        eliminar: $scope.Cajerodao.eliminar,
    };
    $http.post(api_path + 'Cajerodao',data);
    window.location.href = '#/Cajerodao';
  };

  $scope.cancel = function(){
    window.location.href = '#/Cajerodao';
  };
  });