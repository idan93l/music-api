pipeline {
    agent any

    environment {
        IMAGE_NAME = "bourree90s/music-api"
        IMAGE_TAG  = "0.3"

        // Use forward slashes for bash on Windows
        KUBECONFIG = "C:/ProgramData/Jenkins/.kube/config"
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

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-bourree90s',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh 'echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('K8s Sanity Check') {
            steps {
                sh 'kubectl --kubeconfig "$KUBECONFIG" get nodes'
                sh 'kubectl --kubeconfig "$KUBECONFIG" get pods -A'
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh 'helm upgrade --install music-api-test helm/music-api --kubeconfig "$KUBECONFIG"'
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}
