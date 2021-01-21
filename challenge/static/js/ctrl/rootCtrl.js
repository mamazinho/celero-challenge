challenge.controller('RootCtrl', function($scope, $rootScope){

    $scope.__init__ = function(){
      $rootScope.active_tab = 'sites'
      window.errorMessage = ''
    }
  
    $scope.__init__()
  
  })
  