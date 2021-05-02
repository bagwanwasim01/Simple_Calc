pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile calc.py'
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
                sh 'py.test --junit-xml test-reports/results.xml test_calc.py'
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
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                dir(path: env.BUILD_ID) { 
                    unstash(name: 'compiled-results') 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F calc.py'" 
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/calc" 
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}

// pipeline {
//     agent any
//     stages {
//         stage('Checkout'){
//                 steps{
//                     checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '58e8e6a2-9dfe-4cf1-b89f-d4332dc6a841', url: 'https://github.com/bagwanwasim01/Simple_Calc.git']]])        
//                 }            
//         }
//         stage('Build') {
//            steps {
//                git branch: 'main', credentialsId: '58e8e6a2-9dfe-4cf1-b89f-d4332dc6a841', url: 'https://github.com/bagwanwasim01/Simple_Calc.git'
//                sh 'python calc.py'
//            }
//         }
//         stage('Test') {
//             steps {
//                  sh 'python test_calc.py'
//              }
//          }
//     }
// }
        