challenge.controller('AthletesCtrl', function($scope, HttpFctr){

  $scope.__init__ = function(){
    $scope.athletes = []
    $scope.treeIds = []
    $scope.openCreateModal = false
    $scope.openEditModal = false
    $scope.createAthlete = {
      'name': '',
      'users': '',
      'parent': '',
      'percent': '',
      'status': '',
    }
    $scope.editAthlete = {
      'id': '',
      'name': '',
      'users': '',
      'parent': '',
      'percent': '',
      'status': '',
    }
    $scope.getAthletes()
  }

  // Get the Athletes from API
  $scope.getAthletes = function() {
    HttpFctr('athletes', 'GET').then(function(response){
      $scope.athletes = response
      console.log('hhhh', response)
    })
  }

  // Create new Athletes on API
  $scope.createNewAthlete = function() {
    var data = JSON.stringify($scope.createAthlete)
    HttpFctr('athletes', 'POST', {data}).then(function(){
      $scope.getAthletes()
      $scope.openCreateModal = false
      $scope.createAthlete = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  $scope.updateAthlete = function() {
    var data = JSON.stringify($scope.editAthlete)
    HttpFctr(`athletes/${$scope.editAthlete.id}`, 'PUT', {data}).then(function(){
      $scope.getAthletes()
      $scope.openEditModal = false
      $scope.editAthlete = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  $scope.deleteAthlete = function(athlete_id) {
    HttpFctr(`athletes/${athlete_id}`, 'DELETE').then(function(){
      $scope.getAthletes()
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  $scope.editModal = function(athlete) {
    $scope.openEditModal = true
    $scope.editAthlete.id = athlete.id
    $scope.editAthlete.name = athlete.name
    $scope.editAthlete.users = athlete.users
    $scope.editAthlete.parent = athlete.parent
    $scope.editAthlete.percent = athlete.percent
    $scope.editAthlete.status = athlete.status
  }

  $scope.__init__()

})
