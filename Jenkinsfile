pipeline {
    agent any

    environment {
        IMAGE_NAME = "bourree90s/music-api"
        IMAGE_TAG  = "0.3"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh 'helm upgrade --install music-api-test helm/music-api'
            }
        }
    }
}
