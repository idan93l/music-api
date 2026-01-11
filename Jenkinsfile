pipeline {
  agent any

  environment {
    IMAGE_NAME = "bourree90s/music-api"
    IMAGE_TAG  = "0.3"
    RELEASE    = "music-api-test"
    CHART_DIR  = "helm/music-api"
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

    stage('Deploy with Helm') {
      steps {
        sh 'helm upgrade --install $RELEASE $CHART_DIR'
      }
    }
  }

  post {
    always {
      sh 'docker logout || true'
    }
  }
}
