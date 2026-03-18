pipeline {
    agent any

    environment {
        // Defining variables
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                // Gets the code from GitHub
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                bat '''
                "C:\\Users\\sahan\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running basic checks...'
                // We don't have a test suite currently, so we'll just check if app.py compiles correctly
                bat '''
                call venv\\Scripts\\activate.bat
                python -m py_compile app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // In a real environment, this stage would push to a server or build a Docker container.
                echo 'Application deployed successfully (Simulation).'
            }
        }
    }
}
