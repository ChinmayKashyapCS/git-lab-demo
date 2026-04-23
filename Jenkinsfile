pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                    git "https://github.com/ChinmayKashyapCS/git-lab-demo.git"

            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t python-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 python-app'
            }
        }
    }
}
