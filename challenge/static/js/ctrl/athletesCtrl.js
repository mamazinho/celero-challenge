challenge.controller('AthletesCtrl', function($scope, HttpFctr, $rootScope){

  $scope.__init__ = function(){
    $scope.athletes = []
    $scope.treeIds = []
    $scope.secondTreeIds = []
    $scope.thirdTreeIds = []
    $scope.filter_name = ''
    $scope.renderHeader = 'generic'
    $scope.openCreateAthleteModal = false
    $scope.openEditAthleteModal = false
    $scope.openCreateInfosModal = false
    $scope.openEditInfosModal = false
    $scope.createAthlete = {
      'athlete_name': '',
    }
    $scope.createInfosAthlete = {
      'athlete': '',
      'sex': '',
      'age': 0,
      'height': 0,
      'weight': 0,
      'team': '',
      'medal': '',
      'event': ''
    }
    $scope.editAthlete = {
      'id': '',
      'athlete_name': '',
    }
    $scope.editInfosAthlete = {
      'id': '',
      'age': 0,
      'sex': '',
      'height': 0,
      'weight': 0,
      'team': '',
      'medal': '',
      'event': ''
    }
    $scope.offset_next = null,
    $scope.offset_prev = null,
    $scope.actual_offset = null
    $scope.params = {
      'limit': 10,
      'limitoffset': 20,
      'offset': null,
      'athlete_name': null
    }
    $scope.getAthletes()
  }

  // Get the Athletes from API
  $scope.getAthletes = function(goTo) {
    if (goTo)
      $scope.params.offset = goTo == 'next' ? $scope.offset_next : $scope.offset_prev
    else
      $scope.params.offset = $scope.actual_offset
    $scope.actual_offset =  $scope.params.offset
    HttpFctr('athletes', 'GET', {params: $scope.params}).then(function(response){
      $scope.athletes = response.results
      $scope.params.athlete_name = null
      $scope.offset_next = response.next ? new URL(response.next).searchParams.get('offset') : null
      $scope.offset_prev = response.previous ? new URL(response.previous).searchParams.get('offset') : null
    })
  }

  // Create new Athletes on API
  $scope.createNewAthlete = function() {
    var data = JSON.stringify($scope.createAthlete)
    HttpFctr('athletes', 'POST', {data}).then(function(){
      $scope.getAthletes()
      $scope.openCreateAthleteModal = false
      $scope.createAthlete = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  // Update Athlete
  $scope.updateAthlete = function() {
    var data = JSON.stringify($scope.editAthlete)
    HttpFctr(`athletes/${$scope.editAthlete.id}`, 'PUT', {data}).then(function(){
      $scope.getAthletes()
      $scope.openEditAthleteModal = false
      $scope.editAthlete = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  // Delete Athlete
  $scope.deleteAthlete = function(athlete_id) {
    HttpFctr(`athletes/${athlete_id}`, 'DELETE').then(function(){
      $scope.getAthletes()
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  // Create new atlhete infos
  $scope.createInfos = function() {
    $scope.createInfosAthlete.medal == '' ? $scope.createInfosAthlete.medal = null : $scope.createInfosAthlete.medal
    $scope.createInfosAthlete.event = [$scope.createInfosAthlete.event]
    var data = JSON.stringify($scope.createInfosAthlete)
    HttpFctr('athletes-infos', 'POST', {data}).then(function(){
      $scope.getAthletes()
      $scope.openCreateInfosModal = false
      $scope.createInfosAthlete = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  // Update Infos Athlete
  $scope.updateInfos = function() {
    var method = 'PATCH'
    $scope.editInfosAthlete.medal == '' ? $scope.editInfosAthlete.medal = null : $scope.editInfosAthlete.medal
    $scope.editInfosAthlete.event = $scope.editInfosAthlete.event ? [$scope.editInfosAthlete.event] : null
    console.log($scope.editInfosAthlete.event)
    if ($scope.editInfosAthlete.event)
      method = 'PUT'
    var data = JSON.stringify($scope.editInfosAthlete)
    HttpFctr(`athletes-infos/${$scope.editInfosAthlete.id}`, method, {data}).then(function(){
      $scope.getAthletes()
      $scope.openEditInfosModal = false
      $scope.editInfosAthlete = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  // Delete Infos Athlete
  $scope.deleteInfos = function(infos_id) {
    HttpFctr(`athletes-infos/${infos_id}`, 'DELETE').then(function(){
      $scope.getAthletes()
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  $scope.editAthleteModal = function(athlete) {
    $scope.openEditAthleteModal = true
    $scope.editAthlete.id = athlete.id
    $scope.editAthlete.athlete_name = athlete.athlete_name
  }
  $scope.editInfosModal = function(infos) {
    $scope.openEditInfosModal = true
    $scope.editInfosAthlete.id = infos.id
    $scope.editInfosAthlete.athlete = infos.athlete
    $scope.editInfosAthlete.sex = infos.sex
    $scope.editInfosAthlete.age = infos.age
    $scope.editInfosAthlete.height = infos.height
    $scope.editInfosAthlete.weight = infos.weight
    $scope.editInfosAthlete.team = infos.team
    $scope.editInfosAthlete.medal = infos.medal
  }

  $scope.viewMore = function(treeStr, id) {
    tree = eval(`$scope.${treeStr}`)
    if (!tree.includes(id)) {
      tree.push(id)
      if (treeStr == 'treeIds')
        $scope.renderHeader = 'athlete_infos'
      else if (treeStr == 'secondTreeIds')
        $scope.renderHeader = 'event'

    } else {
      tree.splice(tree.findIndex((item) => item == id), 1)
      if (treeStr == 'treeIds')
        $scope.renderHeader = 'generic'
      else if (treeStr == 'secondTreeIds')
        $scope.renderHeader = 'athlete_infos'
    }
  }

  $scope.__init__()

})
