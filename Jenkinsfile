pipeline {
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            agent {
                docker {
                    image 'cimg/python:3.11.4'
                    working_directory '~/repo'
                }
            }
            steps {
                sh 'mvn clean install'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate'
                sh 'pytest'
            }
        }
    }
}
