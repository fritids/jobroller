angular.module('caco.MiniRSS')
    .controller('FeedListCtrl', function ($scope, FeedList) {
        $scope.feeds = new Array({
                url: 'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&output=rss',
                title: 'French google news feeds',
                id: 0
            });

        $scope.$on('FeedList', function (event, data) {
            $scope.feeds = data;
        });
    });