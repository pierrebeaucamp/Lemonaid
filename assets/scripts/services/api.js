Scotiafront.service('API', ['$http', function ($http) {
	// Use x-www-form-urlencoded Content-Type for POST and PUT requests 
	$http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
	$http.defaults.headers.put['Content-Type']  = 'application/x-www-form-urlencoded;charset=utf-8';

	/**
	 * Converts an object to x-www-form-urlencoded serialization.
	 */ 
	var encodeParam = function(obj) {
		var query = '', name, value, fullSubName, subName, subValue, innerObj, i;

		for(name in obj) {
			value = obj[name];

			if(value instanceof Array) {
				for(i=0; i<value.length; ++i) {
					subValue = value[i];
					fullSubName = name + '[' + i + ']';
					innerObj = {};
					innerObj[fullSubName] = subValue;
					query += encodeParam(innerObj) + '&';
				}
			}
			else if(value instanceof Object) {
				for(subName in value) {
					subValue = value[subName];
					fullSubName = name + '[' + subName + ']';
					innerObj = {};
					innerObj[fullSubName] = subValue;
					query += encodeParam(innerObj) + '&';
				}
			}
			else if(value !== undefined && value !== null) {
				query += encodeURIComponent(name) + '=' + encodeURIComponent(value) + '&';
			}
		}

		return query.length ? query.substr(0, query.length - 1) : query;
	};

	// Override $http service's default transformRequest
	$http.defaults.transformRequest = [function(data) {
		return angular.isObject(data) && String(data) !== '[object File]' ? encodeParam(data) : data;
	}];

	var baseRoute = '/';

	// Create and return API service object
	return {
		postLogin: function(credentials) {
			return $http.post(baseRoute + '', credentials).then(function(response) {
				if (response.status === 200) {
					return response.data;
				}
				else {
					alert('ERROR: ' + response.status);
				}
			});
		},

		postLogout: function() {
			return $http.post(baseRoute + '').then(function(response) {
				if (response.status === 200) {
					return response.data;
				}
				else {
					alert('ERROR: ' + response.status);
				}
			});
		},

		postNewAccountInfo: function(info) {
			return $http.post(baseRoute + '', info).then(function(response) {
				if (response.status === 200) {
					return response.data;
				}
				else {
					alert('ERROR: ' + response.status);
				}
			});
		},

		getUserByID: function(userid) {
			var obj = {
				userid: userid
			};

			return $http.post(baseRoute + '', obj).then(function(response) {
				if (response.status === 200) {
					return response.data;
				}
				else {
					alert('ERROR: ' + response.status);
				}
			});
		}
	};
}]);