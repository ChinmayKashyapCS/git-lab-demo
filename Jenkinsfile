pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                    git "https://github.com/ChinmayKashyapCS/git-lab-demo.git"

            }
        stage('Test')
            {
                sh "javac BankService.java"
                sh "java BankService"
        }
    }
}
