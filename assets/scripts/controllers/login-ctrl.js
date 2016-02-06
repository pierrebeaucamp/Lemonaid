Scotiafront.controller('LoginCtrl', ['$scope', '$rootScope', '$window', 'API', function($scope, $rootScope, $window, API) {
	$scope.credentials = {
		'email': null,
		'password': null
	};

	$scope.attemptLogin = function() {
		if (!!$scope.credentials.email && !!$scope.credentials.password) {
			API.postLogin($scope.credentials).then(function(data) {
				if (data.result === true) {
					$window.location.href = '/#/profile/';
				}
				else {
					$scope.loginError = 'Incorrect login credentials';
				}
			});
		}
	};
}]);