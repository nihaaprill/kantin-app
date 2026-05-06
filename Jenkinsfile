pipeline {
    agent any

    environment {
        DOCKER_USER = "USERNAME_DOCKER_KAMU"
        GIT_REPO_URL = "URL_REPO_GITHUB_KAMU.git"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: "${GIT_REPO_URL}"
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-login',
                    passwordVariable: 'PASS',
                    usernameVariable: 'USER'
                )]) {

                    sh "docker build -t ${USER}/film-backend:latest ./backend"
                    sh "docker build -t ${USER}/film-frontend:latest ./frontend"

                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"

                    sh "docker push ${USER}/film-backend:latest"
                    sh "docker push ${USER}/film-frontend:latest"
                }
            }
        }

        stage('Deploy ke Azure AKS') {
            steps {
                withKubeConfig([credentialsId: 'aks-config']) {
                    sh "kubectl apply -f film-k8s.yaml"
                    sh "kubectl rollout restart deployment backend-film"
                    sh "kubectl rollout restart deployment frontend-film"
                }
            }
        }
    }
}