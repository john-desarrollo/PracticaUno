pipeline {
    agent any

    stages {
        stage('Preparar') {
            steps {
                echo 'Preparando el entorno...'
                // Limpia el espacio de trabajo antes de comenzar
                cleanWs()
            }
        }
        stage('Instalar Dependencias') {
            steps {
                echo 'Instalando dependencias...'
                // Instala las dependencias definidas en requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                echo 'Ejecutando pruebas...'
                // Ejecuta los tests, asumiendo que se usa pytest
                sh 'pytest tests'
            }
        }
        stage('Empaquetar') {
            steps {
                echo 'Empaquetando la aplicación...'
                // Empaqueta la aplicación, este paso puede variar según tus necesidades
                sh 'tar -czf my-python-app.tar.gz palindromoapp.py'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finalizado.'
        }
        success {
            echo 'Pipeline exitoso!'
        }
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}


    
