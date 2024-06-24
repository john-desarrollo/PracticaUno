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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                echo 'Ejecutando pruebas...'
                sh 'pytest tests'
            }
        }
        stage('Ejecutar Script') {
            steps {
                echo 'Ejecutando el script principal...'
                input message: 'Ingrese una palabra:', ok: 'Continuar', parameters: [string(defaultValue: 'radar', description: 'Palabra a verificar', name: 'PALABRA')]
                script {
                    def palabra = params.PALABRA
                    sh "python palindromo.py <<< ${palabra}"
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

    
