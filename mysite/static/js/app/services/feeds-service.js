Blog.factory('FeedLoad', function ($resource) {
        return $resource('http://ajax.googleapis.com/ajax/services/feed/load', {}, {
            fetch: { method: 'JSONP', params: {v: '1.0', callback: 'JSON_CALLBACK'} }
        });
    })
    .factory('UrlLookup', function ($resource) {
        return $resource('http://ajax.googleapis.com/ajax/services/feed/lookup', {}, {
            fetch: { method: 'JSONP', params: {v: '1.0', callback: 'JSON_CALLBACK'} }
        });
    });



Blog.service('FeedList', function ($rootScope) {
        
        this.get = function () {
        
            return {
                url: 'http://news.google.fr/news?pz=1&cf=all&ned=fr&hl=fr&output=rss',
                title: 'French google news feed ',
                id: 0
            }
        };

});