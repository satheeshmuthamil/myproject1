pipeline{
    agent{
        label 'winAMD64'
    }
    stages{
        stage('checkout'){
            git 'https://github.com/satheeshmuthamil/myproject1.git'
        }
        stage('build'){
            bat 'type text.txt'
        }
    }
}