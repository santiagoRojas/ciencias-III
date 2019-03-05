'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarDaopersonaCtrl
 * @description
 * # AgregarDaopersonaCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarDaopersonaCtrl', function ($scope, $http) {
    $scope.title = 'Daopersona';
    $scope.message = 'Agregar Daopersona';

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
      if($scope.DaoPersona.consultar == null){
        return;
      }
      if($scope.DaoPersona.eliminar == null){
        return;
      }
      if($scope.DaoPersona.insertar == null){
        return;
      }
      if($scope.DaoPersona.modificar == null){
        return;
      }
    var data = {
        consultar: $scope.DaoPersona.consultar,
        eliminar: $scope.DaoPersona.eliminar,
        insertar: $scope.DaoPersona.insertar,
        modificar: $scope.DaoPersona.modificar,
    };
    $http.post(api_path + 'DaoPersona',data);
    window.location.href = '#/DaoPersona';
  };

  $scope.cancel = function(){
    window.location.href = '#/DaoPersona';
  };
  });