challenge.controller('EventCtrl', function($scope, HttpFctr, $rootScope){

  $scope.__init__ = function(){
    $scope.athletes = []
    $scope.treeIds = []
    $scope.secondTreeIds = []
    $scope.filter_name = ''
    $scope.renderHeader = 'eventInEvent'
    $scope.openCreateEventModal = false
    $scope.openEditEventModal = false
    $scope.createEvent = {
      'event_name': '',
      'city': '',
      'sport': '',
      'year': '',
      'season': '',
      'games': '',
    }
    $scope.editEvent = {
      'id': '',
      'event_name': '',
      'city': '',
      'sport': '',
      'year': '',
      'season': '',
      'games': '',
    }
    $scope.offset_next = null,
    $scope.offset_prev = null,
    $scope.actual_offset = null
    $scope.params = {
      'limit': 10,
      'limitoffset': 20,
      'offset': null,
      'event_name': null
    }
    $scope.getEvents()
  }

  // Get the Events from API
  $scope.getEvents = function(goTo) {
    if (goTo)
      $scope.params.offset = goTo == 'next' ? $scope.offset_next : $scope.offset_prev
    else
      $scope.params.offset = $scope.actual_offset
    $scope.actual_offset =  $scope.params.offset
    HttpFctr('events', 'GET', {params: $scope.params}).then(function(response){
      $scope.events = response.results
      $scope.params.event_name = null
      $scope.offset_next = response.next ? new URL(response.next).searchParams.get('offset') : null
      $scope.offset_prev = response.previous ? new URL(response.previous).searchParams.get('offset') : null
    })
  }
  // Create new Event on API
  $scope.createNewEvent = function() {
    $scope.createEvent.games = `${$scope.createEvent.year} ${$scope.createEvent.season}`
    var data = JSON.stringify($scope.createEvent)
    HttpFctr('events', 'POST', {data}).then(function(){
      $scope.getEvents()
      $scope.openCreateEventModal = false
      $scope.createEvent = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  // Update Event
  $scope.updateEvent = function() {
    var data = JSON.stringify($scope.editEvent)
    HttpFctr(`events/${$scope.editEvent.id}`, 'PUT', {data}).then(function(){
      $scope.getEvents()
      $scope.openEditEventModal = false
      $scope.editEvent = {}
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  // Delete Event
  $scope.deleteEvent = function(athlete_id) {
    HttpFctr(`events/${athlete_id}`, 'DELETE').then(function(){
      $scope.getEvents()
    }).catch((error) => {
      console.log('ERROR >>', error)
      alert(window.errorMessage)
    })
  }

  $scope.editEventModal = function(infos) {
    $scope.openEditEventModal = true
    $scope.editEvent.id = infos.id
    $scope.editEvent.event_name = infos.event_name
    $scope.editEvent.city = infos.city
    $scope.editEvent.sport = infos.sport
    $scope.editEvent.year = infos.year
    $scope.editEvent.season = infos.season
    $scope.editEvent.games = infos.games
  }

  $scope.viewMore = function(treeStr, id) {
    tree = eval(`$scope.${treeStr}`)
    if (!tree.includes(id)) {
      tree.push(id)
      if (treeStr == 'treeIds')
        $scope.renderHeader = 'infosInEvent'
    } else {
      tree.splice(tree.findIndex((item) => item == id), 1)
      if (treeStr == 'treeIds')
        $scope.renderHeader = 'eventInEvent'
      else if (treeStr == 'secondTreeIds')
        $scope.renderHeader = 'infosInEvent'
    }
  }

  $scope.__init__()

})
