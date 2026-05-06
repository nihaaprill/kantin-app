pipeline {
    agent any

    environment {
        DOCKER_USER = "nihaapril"
        GIT_REPO_URL = "https://github.com/nihaaprill/kantin-app.git"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: "${GIT_REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_USER}/film-backend:latest ./backend"
                sh "docker build -t ${DOCKER_USER}/film-frontend:latest ./frontend"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-login', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    sh "docker push ${USER}/film-backend:latest"
                    sh "docker push ${USER}/film-frontend:latest"
                }
            }
        }
    }
}