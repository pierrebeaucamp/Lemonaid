Scotiafront.controller('ProfileCtrl', ['$scope', '$routeParams', 'API', function($scope, $routeParams, API) {
	API.getUserByID($routeParams.userid).then(function(data) {
		$scope.user = data;
	});

	
}]);