pipeline{
    agent any

    stages{
        stage("Clonning from github"){
            steps{
                script{
                    echo 'Clonning from github .........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/shanks1554/AniStack.git']])
                }
            }
        }
    }
}