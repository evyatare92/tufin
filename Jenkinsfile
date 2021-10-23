pipeline {
    agent any
    stages{
		stage('Build Image'){
			steps {
                sh 'python docker/script.sh'
			}
		}
	}		     
}
