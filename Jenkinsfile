pipeline {
    agent any

    stages {
        stage('Run') {
            steps {
                script {
                    // Solicitar entrada al usuario
                    def userInput = input(
                        id: 'userInput', 
                        message: 'Ingresa una palabra:',
                        parameters: [string(defaultValue: '', description: 'Palabra a verificar')]
                    )

                    // Ejecutar el contenedor Docker y pasar la palabra como argumento
                    bat "docker run --rm palindromo-app python /app/palindromo.py '${userInput}'"
                }
            }
        }
    }
}
