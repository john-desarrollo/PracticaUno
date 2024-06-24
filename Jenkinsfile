pipeline {
    agent any

    parameters {
        string(name: 'palabra_usuario', defaultValue: '', description: 'Palabra a verificar si es un palíndromo')
    }

    stages {
        stage('Ejecutar Script Python') {
            steps {
                script {
                    def scriptPath = "${WORKSPACE}/script_palindromo.py"
                    def userInput = params.palabra_usuario

                    echo "Palabra ingresada por el usuario: ${userInput}"
                    sh "echo ${userInput} | python3 ${scriptPath}"
                }
            }
        }
    }
}
