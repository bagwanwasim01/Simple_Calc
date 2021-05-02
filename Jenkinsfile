pipeline {
    agent any
    stages {
        stage('Checkout'){
                steps{
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '58e8e6a2-9dfe-4cf1-b89f-d4332dc6a841', url: 'https://github.com/bagwanwasim01/Simple_Calc.git']]])        
                }            
        }
        stage('Build') {
           steps {
               git branch: 'main', credentialsId: '58e8e6a2-9dfe-4cf1-b89f-d4332dc6a841', url: 'https://github.com/bagwanwasim01/Simple_Calc.git'
               bat 'python calc.py test_calc.py'
           }
        }
        stage('Test') {
            steps {
                echo 'job has been tested'
            }
        }
    }
}
        