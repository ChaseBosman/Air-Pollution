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
                sh 'python3 -m py_compile sources/windows.py sources/pollut_api.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}