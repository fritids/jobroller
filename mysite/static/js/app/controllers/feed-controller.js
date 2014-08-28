//A controller to manage the list of posts, and create new ones
// posts in the params is brought from the dependency injected in the router ( in app.js)

Blog.controller('FeedController', function($scope, GlobalService, posts){
	
	$scope.posts = posts;
	$scope.globals = GlobalService;
	// opts for modal
	$scope.opts = {
		backdropFade : true,
		dialogFade: true
	}
	
	
	
})
