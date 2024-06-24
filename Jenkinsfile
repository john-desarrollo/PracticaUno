pipeline {
    agent any

    stages {
        stage('Preparar') {
            steps {
                echo 'Preparando el entorno...'
                cleanWs()  // Limpia el espacio de trabajo antes de comenzar
            }
        }
        stage('Instalar Dependencias') {
            steps {
                echo 'Instalando dependencias...'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                echo 'Ejecutando pruebas...'
                bat 'pytest tests'
            }
        }
        stage('Ejecutar Script') {
            steps {
                echo 'Ejecutando el script principal...'
                script {
                    def palabra = input message: 'Ingrese una palabra:', ok: 'Continuar', parameters: [string(defaultValue: 'radar', description: 'Palabra a verificar', name: 'PALABRA')]
                    bat "echo ${palabra} | python palindromo.py"
                }
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
