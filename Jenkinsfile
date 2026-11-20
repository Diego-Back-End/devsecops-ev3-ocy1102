pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                    if [ ! -d venv ]; then
                        python3 -m venv venv
                    fi
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'venv/bin/python -m unittest test_app.py'
            }
        }

        stage('Security Scan') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'venv/bin/pip install bandit'
                    sh 'venv/bin/bandit -r app.py -f txt'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'nohup python app.py > app.log 2>&1 &'
                echo 'Deploy completado: la aplicación se ejecuta en segundo plano'
            }
        }

        stage('OWASP ZAP') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh '''
                        docker run --rm --network container:jenkins \
                          -v jenkins_home:/zap/wrk \
                          zaproxy/zap-stable zap-baseline.py \
                          -t "http://localhost:5000/hello?name=Diego" \
                          -r zap_report.html
                    '''
                }
            }
        }
    }
}
