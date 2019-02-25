'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarConexionCtrl
 * @description
 * # AgregarConexionCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarConexionCtrl', function ($scope, $http) {
    $scope.title = 'Conexion';
    $scope.message = 'Agregar Conexion';

      $http.get(api_path + 'baseDeDatos?limit=0')
      .then(function(response) {
        $scope.baseDeDatos = response.data;
      });
      $http.get(api_path + 'usuario?limit=0')
      .then(function(response) {
        $scope.usuario = response.data;
      });
      $http.get(api_path + 'contase�a?limit=0')
      .then(function(response) {
        $scope.contase�a = response.data;
      });

    $scope.add = function(){
      if($scope.Conexion.baseDeDatos == null){
        return;
      }
      if($scope.Conexion.usuario == null){
        return;
      }
      if($scope.Conexion.contase�a == null){
        return;
      }
    var data = {
        baseDeDatos: $scope.Conexion.baseDeDatos,
        usuario: $scope.Conexion.usuario,
        contase�a: $scope.Conexion.contase�a,
    };
    $http.post(api_path + 'Conexion',data);
    window.location.href = '#/Conexion';
  };

  $scope.cancel = function(){
    window.location.href = '#/Conexion';
  };
  });