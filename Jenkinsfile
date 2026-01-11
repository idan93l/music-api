pipeline {
  agent any

  environment {
    IMAGE_NAME  = "bourree90s/music-api"
    IMAGE_TAG   = "0.3"

    // IMPORTANT: this is the kubeconfig file we created on Windows for the Jenkins service
    KUBECONFIG  = "C:\\ProgramData\\Jenkins\\.kube\\config"
  }

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Build Docker Image') {
      steps { sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .' }
    }

    stage('Docker Login') {
      steps {
        withCredentials([string(credentialsId: 'dockerhub-token', variable: 'DOCKERHUB_TOKEN')]) {
          sh 'echo $DOCKERHUB_TOKEN | docker login -u bourree90s --password-stdin'
        }
      }
    }

    stage('Push Docker Image') {
      steps { sh 'docker push $IMAGE_NAME:$IMAGE_TAG' }
    }

    stage('Deploy with Helm') {
      steps {
        // prove Jenkins can reach the cluster (this is the exact thing that failed before)
        sh 'kubectl --kubeconfig "$KUBECONFIG" get nodes'

        // helm should use the same kubeconfig
        sh 'helm --kubeconfig "$KUBECONFIG" upgrade --install music-api-test helm/music-api'
      }
    }
  }

  post {
    always {
      sh 'docker logout || true'
    }
  }
}

