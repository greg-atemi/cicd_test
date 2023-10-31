pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
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
