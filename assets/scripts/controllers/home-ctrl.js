Scotiafront.controller('HomeCtrl', ['$scope', '$rootScope', 'API', function($scope, $rootScope, API) {
	$scope.info = {
		'email': null,
		'password': null,
		'amount': null,
		'score': null
	};

	$scope.attemptNewAccountCreation = function() {
		if (!!$scope.info.email && !!$scope.info.password && !!$scope.info.amount && !!$scope.info.score) {
			API.postNewAccountInfo($scope.info).then(function(data) {
				if (data.result === true) {
					$window.location.href = '/#/creditinfo/';
				}
				else {
					$scope.loginError = 'Incorrect login credentials';
				}
			});
		}
	};
}]);