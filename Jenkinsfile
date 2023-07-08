pipeline {
  agent any
  stages {
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      sh"docker build -t try_again_tests ."
      	     }
          }
       }
    }
     stage('Pull browser') {
        steps {
           catchError {
              script {
      	    docker.image('selenoid/chrome:114.0')
      	      }
           }
        }
     }
     stage('Run tests') {
        steps {
           sh"""
           docker run -it try_again_tests --bversion ${bversion}
           --executor ${executor} --browser ${browser}
           --url_opencart ${url_opencart}
           """
         }
     }
     stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'report']]
    	   ])
  	        }
         }
     }
}
