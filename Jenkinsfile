pipeline {
    agent { docker { image 'python:3.7.7-buster' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}