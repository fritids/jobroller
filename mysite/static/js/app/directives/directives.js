// bar that shows when the user try to switch to another view
Blog.directive('pendingBar', function($rootScope){
	return{
		link: function (scope, element, attrs) {
                element.addClass('hide');
                
                // everyone of the states -routeChangeStart,...- goes with the resolve on the state provider
                $rootScope.$on('$routeChangeStart', function () {
                    element.removeClass('hide');
                });
                $rootScope.$on('$routeChangeSuccess', function () {
                    element.addClass('hide');
                });
                $rootScope.$on('$routeChangeError', function () {
                    element.removeClass('hide');
                });
            }
	}

});
// This hides the view until the routing is completed.
Blog.directive('viewState', ['$rootScope',
    function ($rootScope) {
        return {
            link: function (scope, element, attrs) {
                element.addClass('hide');
                $rootScope.$on('$routeChangeStart', function () {
                    element.addClass('hide');
                });
                $rootScope.$on('$routeChangeSuccess', function () {
                    element.removeClass('hide');
                });
                $rootScope.$on('$routeChangeError', function () {
                    element.addClass('hide');
                });
            }
        };
}]);

Blog.directive('showTab', function () {
    return{
        link: function (scope, element, attrs) {
            element.on('click',function (e) {
                e.preventDefault();
                element.tab('show');
                console.log("this clicked");
                window.el = element;
            })
        }
    }
})