pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.7.2' 
                }
            }
            steps {
                sh 'python3 -m py_compile windows.py pollut_api.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
    }
}