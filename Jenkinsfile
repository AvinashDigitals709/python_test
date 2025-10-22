pipeline {
    agent any

    stages {
        stage('Checkout') {
             steps {
                git branch: 'main', url: 'https://github.com/AvinashDigitals709/python_test.git'
            }
        }


        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 main.py'
            }
        }

        
    }

    post {
        always {
            echo 'Build completed!'
        }
    }
}
