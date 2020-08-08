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
                sh 'python3 -m py_compile src/controller.py src/pollut_api.py src/calculations.py src/user_input.py src/print_carbon_footprint.py src/main_window_select.py' 
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
                sh 'py.test --junit-xml test-reports/results.xml tests/calc_unit_test.py tests/api_integration_test.py tests/user_input_test.py tests/controller_integration_test.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}