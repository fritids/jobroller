// object for accessing a Post object of our REST API.

Blog.factory('PostService', function($http, $q, $timeout){
	var api_url = "/posts/";
	
	return{
		list : function(){
			var defer = $q.defer();

			// (Look at Angularjs Fundamentals video and search $location tut to learn how to clear the hostory cache)
			// this resource is delayed 2 sec  
			// $timeout(function  () {
				
				

			// }, 500)

			$http( { method: 'GET', url : api_url } ).
				success(function(data, status, headers, config){
					defer.resolve(data);
				}).
				error(function(data, status, headers, config){
					defer.reject(status);
				});
			
			// if we do not generate the promise, we can not call .then later
			return defer.promise;
				
		},// end list
		
		get: function(post_id){
			var url = api_url + post_id + "/";
			var defer = $q.defer();
			$http( { method:'GET', url:url } ).
				success(function(data, status, headers, config){
					defer.resolve(data);
				}).
				error(function(data, status, headers, config){
					defer.reject(status);
				});
			// if we do not generate the promise, we can not call .then later
			return defer.promise;
		},// end get
		
		update: function (post) {
            var url = api_url + post.id + "/";
            var defer = $q.defer();
            $http({method: 'PUT',
                url: url,
                data: post}).
                success(function (data, status, headers, config) {
					console.log('saved successfully');
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(status);
                });
                
             // if we do not generate the promise, we can not call .then later
            return defer.promise;
        },// end update
        
        save: function (post) {
            var url = api_url;
            var defer = $q.defer();
            $http({method: 'POST',
                url: url,
                data: post}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(status);
                });
                
            // if we do not generate the promise, we can not call .then later
            return defer.promise;
        }, // end save
        
        delete: function(post){
			console.log('in service');
			console.log(post);
			var url = api_url + post + '/';
			var defer = $q.defer();
			$http({ method:'DELETE', url:url }).
			success(function(data, status, headers, config){
				defer.resolve(data);
				console.log(data);
			}).
			error(function(data, status, headers, config){
				defer.reject(status)
			});
			
			// if we do not generate the promise, we can not call .then later
			return defer.promise;
		}
       
		
			
	}
})
