pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                    git 'https://github.com/ChinmayKashyapCS/git-lab-demo.git'
                    sh 'javac BankService.java'
                    sh 'java BankService'
            }
        }
    }
}
