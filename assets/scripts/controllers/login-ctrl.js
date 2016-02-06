Scotiafront.controller('LoginCtrl', ['$scope', '$rootScope', 'API', function($scope, $rootScope, API) {
	$scope.credentials = {
		'email': null,
		'password': null
	};

	$scope.attemptLogin = function() {
		if ($scope.loginForm.$valid) {
			API.postLogin($scope.credentials).then(function(data) {
				if (data.result === true) {
					
				}
				else {
					$scope.loginError = 'Incorrect login credentials';
				}
			});
		}
	};
}]);