pipeline {
    agent any

    stages {
        stage('Ejecutar Script Python') {
            steps {
                script {
                    def userInput = input(
                        id: 'userInput',
                        message: 'Ingrese una palabra para verificar si es un palíndromo:',
                        parameters: [
                            [$class: 'StringParameterDefinition', defaultValue: '', description: 'Palabra a verificar']
                        ]
                    )
                    
                    sh "echo \"${userInput}\" | python3 ${WORKSPACE}/script_palindromo.py"
                }
            }
        }
    }
}
