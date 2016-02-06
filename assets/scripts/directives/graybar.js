Scotiafront.directive('graybar', ['$window', function($window) {
    return {
        restrict: 'EA',
        templateUrl: '/templates/graybar.html',
        scope: {
			title: '=title'
        }
    };
}]);