(function(){
  angular.module('notifyApp')
    .config(config)

  config.$inject = [
  	'$httpProvider',
  	'$resourceProvider'
  ]

  function config($httpProvider, $resourceProvider){
  	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
  	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFTOKEN';

  	$resourceProvider.defaults.stripTrailingSlashes = false;
  }
})()