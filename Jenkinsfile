pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages{
        stage("Clonning from github"){
            steps{
                script{
                    echo 'Clonning from github .........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/shanks1554/AniStack.git']])
                }
            }
        }

        stage("Making a virtual environment"){
            steps{
                script{
                    echo 'Making a virtual environment .........'
                    sh '''
                        python -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -e .
                        pip install dvc
                    '''
                }
            }
        }

        stage('DVC Pull'){
            steps{
                withCredentials([file(credentialsId:'gcp-key' , variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'DVC Pull .....'
                        sh '''
                            . ${VENV_DIR}/bin/activate
                            dvc pull
                        '''
                    }
                }
            }
        }
    }


}