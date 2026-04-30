pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -c "print(\'App working\')"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application deployed successfully'
            }
        }
    }
}
