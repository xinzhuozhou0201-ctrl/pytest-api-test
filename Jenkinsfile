pipeline {
    agent any

    stages {
        stage('拉取代码') {
            steps {
                checkout scm
            }
        }

        stage('安装依赖') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('执行测试') {
            steps {
                bat 'pytest -v --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            publishHTML([
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: '测试报告',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}