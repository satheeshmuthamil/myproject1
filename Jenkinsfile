pipeline{
    agent{
        label 'winAMD64'
    }
    stages{
        stage('checkout'){
            steps{
                git 'https://github.com/satheeshmuthamil/myproject1.git'
            }
        }
        stage('build'){
            steps{
                bat 'type text.txt'
            }
        }
    }
}
