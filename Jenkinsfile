pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Construir la imagen Docker
                    bat 'docker build -t palindromo-app .'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Ejecutar el contenedor Docker
                    bat 'docker run --rm palindromo-app'
                }
            }
        }
    }
}