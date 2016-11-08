var app=angular.module('app',['controllers']);
var controllers=angular.module('controllers',[]);



controllers.controller('userDetailsController',function($scope,$http)
{
	$http.get('http://127.0.1:3000/index').success(function(data){
		$scope.songs=data;
	});

	$scope.name_filter;

	$scope.categorize=function(type,category){
		var config = { headers : {'Content-Type': 'application/json'}}
		if(category=='genre'){
			data={"genre":type}
		}
		else if(category=='album'){
			data={"album":type}
		}
		else{
			data={"artist":type}
		}

		api='http://127.0.1:3000/'+category+'/'
		$http.post(api, data, config).success(function (res) {
        $scope.songs=res;
      })
		}

		$scope.addToPlaylist = function(song_name){
			var config = { headers : {'Content-Type': 'application/json'}}
			var data = {"name":song_name}
			$http.post('http://127.0.1:3000/playlist/', data, config).success(function (res) {
	        Materialize.toast("Song added to playlist",3000);
	      })
		}

});
