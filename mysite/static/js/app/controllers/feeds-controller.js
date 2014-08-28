// a controller to bring RSS feeds from one url

Blog.controller('FeedsController', function($scope, GlobalService, FeedLoad, FeedList){

	$scope.feed = null;

	var feed = FeedList.get();
	console.log(feed);

	// feed.url = "http://www.lemonde.fr/rss/une.xml";
	// feed.url = 'http://www.aljazeera.net/AljazeeraRss/c992b9df-12d8-42ee-a0b0-f7fa7b2d6df8/3ea5221b-aab2-4774-9417-5416dac996db';
    FeedLoad.fetch({q: feed.url, num: 50}, {}, function (data) {
    	console.log(data);
        $scope.feed = data.responseData.feed;
        $scope.feed.id = feed.id;
        window.ff = $scope.feed;
    });

	// feed.url = "http://www.lemonde.fr/rss/une.xml";

	
})
