(function(){

 angular.module('notifyApp')
    .controller('notifyController', notifyController)

  // inject dependencies
  notifyController.$inject = ['notifyFactory'];

  function notifyController(notifyFactory){
    var nCtrl = this;
    // nCtrl.user_list = [2, 3]
    nCtrl.message = "Hello World";
    nCtrl.submit_form = submit_form;
    notifyFactory.users().query().$promise.then(function(response){
      nCtrl.user_list = response;
    })
    function submit_form(){
      angular.forEach(nCtrl.user_ids, function(element, index) {
        var data = {
          'header': nCtrl.header,
          'content': nCtrl.content,
          'image_url': nCtrl.image,
          'dispatch_time': nCtrl.time,
          'user': element
        }

        notifyFactory.notification().save(data);
      });
    }
  }
})();