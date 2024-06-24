pipeline {
    agent any
    stages {
        stage('Input Stage') {
            steps {
                script {
                    def userInput = input(
                        id: 'userInput', 
                        message: 'Ingresa una palabra:', 
                        parameters: [
                            string(defaultValue: '', description: 'Palabra a verificar')
                        ]
                    )
                    echo "La palabra ingresada es: ${userInput}"
                }
            }
        }
    }
}
