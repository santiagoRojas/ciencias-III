'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarDaocajeroCtrl
 * @description
 * # AgregarDaocajeroCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarDaocajeroCtrl', function ($scope, $http) {
    $scope.title = 'Daocajero';
    $scope.message = 'Agregar Daocajero';

      $http.get(api_path + 'consultar?limit=0')
      .then(function(response) {
        $scope.consultar = response.data;
      });
      $http.get(api_path + 'eliminar?limit=0')
      .then(function(response) {
        $scope.eliminar = response.data;
      });
      $http.get(api_path + 'insertar?limit=0')
      .then(function(response) {
        $scope.insertar = response.data;
      });
      $http.get(api_path + 'modificar?limit=0')
      .then(function(response) {
        $scope.modificar = response.data;
      });

    $scope.add = function(){
      if($scope.DaoCajero.consultar == null){
        return;
      }
      if($scope.DaoCajero.eliminar == null){
        return;
      }
      if($scope.DaoCajero.insertar == null){
        return;
      }
      if($scope.DaoCajero.modificar == null){
        return;
      }
    var data = {
        consultar: $scope.DaoCajero.consultar,
        eliminar: $scope.DaoCajero.eliminar,
        insertar: $scope.DaoCajero.insertar,
        modificar: $scope.DaoCajero.modificar,
    };
    $http.post(api_path + 'DaoCajero',data);
    window.location.href = '#/DaoCajero';
  };

  $scope.cancel = function(){
    window.location.href = '#/DaoCajero';
  };
  });