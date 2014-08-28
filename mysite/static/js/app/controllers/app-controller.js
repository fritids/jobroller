// A controller to initialize our app  (just bring the is_authenticated from app-service.js)
// updated according to the user.is_authenticated in genral.html 

var appController = Blog.controller('AppController', function($scope, $rootScope, GlobalService, $location){
	
	var failureCb = function(status){
		console.log(status);
	};
	
   
	$scope.globals = GlobalService;
	// is_authenticated paramater is the evaluated expression in general.html
	$scope.initialize = function(is_authenticated){
		console.log(is_authenticated);
		$scope.globals.is_authenticated = is_authenticated;
	};
    
	
});
