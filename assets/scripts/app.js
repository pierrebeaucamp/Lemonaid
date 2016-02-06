var Scotiafront = angular.module('Scotiafront', ['ngRoute', "ngAnimate"]);

Scotiafront.config(['$compileProvider', function ($compileProvider) {
	$compileProvider.debugInfoEnabled(false);
}]);

Scotiafront.config(['$routeProvider', function($routeProvider) {
	$routeProvider.when('/', {
        templateUrl: 'static/ng-templates/home.html',
		controller: 'HomeCtrl'
	}).when('/login/', {
        templateUrl: 'static/ng-templates/login.html',
		controller: 'LoginCtrl'
	}).when('/signup/', {
        templateUrl: 'static/ng-templates/signup.html',
		controller: 'SignupCtrl'
	}).otherwise({
		redirectTo: '/'
	});
}]);
