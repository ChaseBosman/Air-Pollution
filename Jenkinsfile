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
                sh 'python3 -m py_compile pollut_api.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
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
  	stage('Deliver') { 
            agent any
            environment { 
		VOLUME = '$(pwd):/src/'
                IMAGE = 'cdrx/pyinstaller-windows:python3'
            }
            steps {
                dir(path: env.BUILD_ID) { 
                    unstash(name: 'compiled-results') 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -c -F --hidden-import=requests pollut_api.py'" 
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/dist/*" 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}