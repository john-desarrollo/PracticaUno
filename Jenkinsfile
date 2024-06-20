pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('palindromoapp') {
      steps {
        sh 'python palindromoapp.py'
      }
    }
  }
}


    
