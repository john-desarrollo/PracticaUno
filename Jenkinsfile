pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/john-desarrollo/PracticaUno.git'
            }
        }

        stage('Build and Run') {
            steps {
                sh 'python3 palindromoapp.py'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
    
