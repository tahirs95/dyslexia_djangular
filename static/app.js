var app = angular.module('quizApp', ['ngRoute']);

app.config(['$httpProvider', function ($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.config(['$routeProvider',function ($routeProvider) {
      $routeProvider
        .when('/', {
          templateUrl: '/static/template.html',
          controller: 'myCtrl'
        })
		.otherwise('/');
	}
]);

app.controller('myCtrl', ['$scope', '$log', '$http', '$filter', 'quizFactory', function($scope, $log, $http, $filter, quizFactory) {
			$scope.start = function() {
				$scope.answerMode = true;
				$scope.Ex();
				$scope.id = 0;
				$scope.quizOver = false;
				$scope.inProgress = true;
				quizFactory.serverCall().then(function(){
					$scope.getQuestion();
				});	
			};

			$scope.reset = function() {
				$scope.inProgress = false;
				$scope.score = 0;
			}

			$scope.Ex = function () {
				//var csrftoken = $.cookie('csrftoken');
					var u, w, v, c, is;
					$http.get("/api/p_login/")
						.then(function (response) {
							$scope.content = response.data;
							c = $scope.content;
							is = c["0"].patient_ID;
							$scope.u = '/api/patients/' + is + '/';
								// console.log(v);
								$http.post("/api/exams/",
								{
									patient_ID : $scope.u
								})
								.error(function(err){
									console.log($scope.u);
									//console.log(err);
								})
								.success(function(response) 
								{
									//console.log("Success")
									//console.log(response);
									//$scope.usersData = response;
								});	
						});	
				};

			$scope.Sc = function() {
				var u, w, v, g, is;
				$http.get("/api/p_login/")
						.then(function (response) {
							$scope.content = response.data;
							g = $scope.content;
							is = g["0"].patient_ID;
							$scope.u = '/api/patients/' + is + '/';
				$http.get("/api/exams/")
						.then(function (response) {
							$scope.content = response.data;
							c = $scope.content;
							var key=c.length;
							var a;
							for(var key in c)
							{
								if(key == c.length-1)
								 {
									console.log(c[key].exam_ID);
									a=c[key].exam_ID;
								 }
							}
							$scope.e = '/api/exams/' + a + '/';
							$http.post("/api/results/",
							{
								p_ID : $scope.u,
								exam_ID: $scope.e,
								hits: $scope.hits,
								misses: $scope.misses,
								accuracy: $scope.accuracy
							})
							.error(function(err){
								console.log(err);
							})
							.success(function(response) 
							{
								console.log("Success")
								console.log(response);
								$scope.usersData = response;
							});
						});
					});		
		};

		$scope.Detailed = function() {
			var u, w, v, c, is, d,a,b;
			$http.get("/api/questions/")
					.then(function (response) {
						$scope.content = response.data;
						c = $scope.content;
						$scope.j=$scope.id+1;
						$scope.d = '/api/questions/' + $scope.j + '/';
						console.log($scope.d);
							// console.log(v);
						$http.get("/api/exams/")
						.then(function (response) {
							$scope.content = response.data;
							b=$scope.content;
							var key=b.length;
							for(var key in b)
							{
								if(key == b.length-1)
								 {
									console.log(b[key].exam_ID);
									a=b[key].exam_ID;
								 }
							}
							$scope.ee = '/api/exams/' + a + '/';
						$http.post("/api/detailed_score/",
						{
							exam_ID: $scope.ee,
							ques_ID: $scope.d,
							answer_submitted: $scope.ans
						})
						.error(function(err){
							console.log(err);
							console.log($scope.d.toString());
							console.log($scope.ee.toString());
							console.log($scope.ans.toString());
						})
						.success(function(response) 
						{
							console.log("Success")
							console.log(response);
							$scope.usersData = response;
						});
					});
				});			
	};

			$scope.getQuestion = function() {
				$scope.q = quizFactory.getQuestion($scope.id);
				if($scope.q) {
					$scope.question = $scope.q.question;
					$scope.aud = $scope.q.aud;
					$scope.aa = new Audio($scope.aud);
					console.log($scope.aa);
					$scope.answer = $scope.q.answer;
					$scope.answerMode = true;
				} else {
					if($scope.quizOver = true){
						$scope.hits = $scope.score;
						$scope.misses = $scope.id-$scope.score;
						$scope.accuracy = (($scope.hits)/$scope.id)*100;
						$scope.Sc();
					}
				}
			};

			$scope.playAud = function() {
				$scope.aa.play();
			};

			$scope.checkAnswer = function() {
				$scope.ans=$filter('lowercase')($scope.ans)
				if($scope.ans == $scope.answer) {
					$scope.score++;
					$scope.correctAns = true;
				} else {
					$scope.correctAns = false;
				}
				$scope.Detailed();
				$scope.answerMode = false;
			};

			$scope.nextQuestion = function() {
				$scope.id++;
				$scope.getQuestion();
				$scope.ans="";
			}
			$scope.reset();
}]);


app.factory('quizFactory', ['$http', function ($http) {
	var questions = [];
	return {
		// 1st function
		serverCall: function () {
			return $http.get('/api/questions').then(function (response) {

				//var questions = [];
				var qu = response.data;
				questions = [];
				for (var i in qu) {
					var item = qu[i];
					questions.push({
						"aud": item.audio,
						"answer": item.correct_answer
					});
				}
			});
		},

		getQuestion: function (id) {
			console.log(id);
			console.log(questions);

			if (id < questions.length) {

				return questions[id];
			} else {
				return false;
			}
		}
	};
}]);