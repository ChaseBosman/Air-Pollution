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
stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --junit-xml test-reports/results.xml calc_unit_test.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }