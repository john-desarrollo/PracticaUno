pipeline {
    agent {
        docker {
            image 'python:3.8'  // Utilizamos la imagen oficial de Python
            args '-u root'      // Argumentos adicionales si son necesarios
        }
    }
    stages {
        stage('Verificar palíndromo') {
            steps {
                sh 'pip install pytest'  // Instalamos pytest si es necesario
                sh 'python palindromo.py' // Ejecutamos el script Python
            }
        }
    }
}