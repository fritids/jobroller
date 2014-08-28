// in the views urls must be prefixed with # to make them different than django urls

'use strict';
var Blog = angular.module("Blog", ["ui.bootstrap", "ngCookies", "ngResource"], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

Blog.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
})

Blog.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/feed.html",
            controller: "FeedController",  // to create modal actions ( create, open, close )

            // this property delays loading a view until we have finished loading its data (the view must provide a promise)
            // this is an optional dependency injected in the controller, if they are promises, the router will wait for them
            resolve: {
                posts: function (PostService) {
                    return PostService.list();
                }
            }
        })
        .when("/post/:id", {
            templateUrl: "static/js/app/views/view.html",
            controller: "PostController",
            resolve: {
                post: function ($route, PostService) {
                    var postId = $route.current.params.id
                    return PostService.get(postId);
                }
            }
        })
        .when("/post/:id/edit", {
			templateUrl: '/static/js/app/views/edit.html',
			controller: 'PostController',
			resolve: {
				post: function($route, PostService){
					var postId = $route.current.params.id;
					return PostService.get(postId);
				}
			}
		})
		
		.when("/new", {
            templateUrl: '/static/js/app/views/new.html',
            controller: 'NewPostController',
            resolve: {
                posts : function(PostService){
                return PostService.list();
                }
            }
        })
        .when("/feeds", {
			templateUrl: '/static/js/app/views/feeds.html',
			controller: 'FeedsController',
			resolve: {
				posts : function(FeedList){
				return FeedList.get;
				}
			}
		})
        .otherwise({
            redirectTo: '/'
        })
});


// resolve : is used to load data before changing the view
// the data workflow:
// appjs, --> feed.html -->  feed-controller(prepare modal window)  --> PostService (to listen to GET request)

// with angular directive, We’ll keep our markup intact by just adding a custom attribute
