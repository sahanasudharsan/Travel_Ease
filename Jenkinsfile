pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat '''
                IF EXIST venv rmdir /s /q venv
                "C:\\Users\\sahan\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                venv\\Scripts\\python -m pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                venv\\Scripts\\python app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment successful (Simulation)'
            }
        }
    }
}
