Blog.controller("NewPostController", function($scope, GlobalService, PostService,  posts){
    
    $scope.posts = posts;
    $scope.globals = GlobalService;
    
    // to avoid doing that we create a copy below (angular.copy )
    //~ $scope.post = {title:'', description: ''};
    
    $scope.create = function (post) {
        $scope.post = angular.copy(post);
        PostService.save($scope.post).then(function (data) {
            $scope.post = data;
            $scope.posts.push(data);
            // resest the form
            $scope.post = {};
        }, function(status){
            console.log(status);
        });
    };
})
