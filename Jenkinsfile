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
                sh 'python3 -m py_compile src/main_window_select.py src/compute_window.py src/api_window.py src/pollution_api.py src/calculation.py' 
                stash(name: 'compiled-results', includes: 'src/*.py*') 
            }
        }
	stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'nosetests --with-xunit'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}