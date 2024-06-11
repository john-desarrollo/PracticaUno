pipeline{
  agent any
    stages{
     
      stage('version'){
        steps{
          sh 'python3 --version'
        }
      } 
      stage('palindromoapp'){
        steps {
          sh 'python3 palindromoapp.py'
        }
      }
    }            
}
    