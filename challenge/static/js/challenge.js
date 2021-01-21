var challenge = angular.module('challenge', [])
challenge.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[')
  $interpolateProvider.endSymbol(']}')
})