'use strict';

/**
 * @ngdoc function
 * @name nameApp.controller:AgregarHoliCtrl
 * @description
 * # AgregarHoliCtrl
 * Controller of the nameApp
 */
angular.module('nameApp')
  .controller('AgregarHoliCtrl', function ($scope, $http) {
    $scope.title = 'Holi';
    $scope.message = 'Agregar Holi';

      $http.get(api_path + 'nombre?limit=0')
      .then(function(response) {
        $scope.nombre = response.data;
      });
      $http.get(api_path + 'apellido?limit=0')
      .then(function(response) {
        $scope.apellido = response.data;
      });
      $http.get(api_path + 'direccion?limit=0')
      .then(function(response) {
        $scope.direccion = response.data;
      });
      $http.get(api_path + 'edad?limit=0')
      .then(function(response) {
        $scope.edad = response.data;
      });
      $http.get(api_path + 'telefono?limit=0')
      .then(function(response) {
        $scope.telefono = response.data;
      });
      $http.get(api_path + 'correo?limit=0')
      .then(function(response) {
        $scope.correo = response.data;
      });
      $http.get(api_path + 'nuevo?limit=0')
      .then(function(response) {
        $scope.nuevo = response.data;
      });

    $scope.add = function(){
      if($scope.Holi.nombre == null){
        return;
      }
      if($scope.Holi.apellido == null){
        return;
      }
      if($scope.Holi.direccion == null){
        return;
      }
      if($scope.Holi.edad == null){
        return;
      }
      if($scope.Holi.telefono == null){
        return;
      }
      if($scope.Holi.correo == null){
        return;
      }
      if($scope.Holi.nuevo == null){
        return;
      }
    var data = {
        nombre: $scope.Holi.nombre,
        apellido: $scope.Holi.apellido,
        direccion: $scope.Holi.direccion,
        edad: $scope.Holi.edad,
        telefono: $scope.Holi.telefono,
        correo: $scope.Holi.correo,
        nuevo: $scope.Holi.nuevo,
    };
    $http.post(api_path + 'Holi',data);
    window.location.href = '#/Holi';
  };

  $scope.cancel = function(){
    window.location.href = '#/Holi';
  };
  });