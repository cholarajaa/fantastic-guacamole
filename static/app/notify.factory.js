(function(){
  angular.module('notifyApp')
    .factory('notifyFactory', notifyFactory);

  function notifyFactory($resource){
  	var factory = {
  		users: users,
      notification: notification
  	}
  	return factory

  	function users(){
  		return $resource('/users/')
  	}

    function notification(){
      return $resource('/notifications/')
    }
  }
})()