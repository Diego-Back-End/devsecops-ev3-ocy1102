pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest test_app.py'
            }
        }

        stage('Security Scan') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'pip install bandit'
                    sh 'bandit -r app.py -f txt'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'nohup python app.py > app.log 2>&1 &'
                echo 'Deploy completado: la aplicación se ejecuta en segundo plano'
            }
        }
    }
}
