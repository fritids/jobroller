// allow to communicate between controllers and hold global (authentication purposes) variables.

Blog.factory('GlobalService', function(){
	var vars = {
			is_authenticated : false
		}
	return vars
})
