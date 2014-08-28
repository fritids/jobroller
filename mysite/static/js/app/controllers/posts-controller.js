//A controller to view and edit a single post

Blog.controller('PostController', function($scope, GlobalService, post, PostService){
    $scope.post = post;
    $scope.globals = GlobalService;
    
    // function needed when update is failed
    var failureCb = function(status){
        console.log(status);
    }
    
    // update post
    $scope.update = function () {
        PostService.update($scope.post).then(function (data) {
            $scope.post = data;
        }, failureCb);
    };
    
    // delete post
    $scope.delete = function (post) {
        $scope.post = angular.copy(post);
        PostService.delete($scope.post.id).then(function(result){
            // redirect after deleting the post
            window.location.href = "/";
        });
    };
    
    
})
