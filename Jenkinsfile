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
                    // Ejecutar el contenedor Docker y pasar una palabra como argumento
                    bat 'docker run --rm palindromo-app python /app/palindromo.py "reconocer"'
                }
            }
        }
    }
}
