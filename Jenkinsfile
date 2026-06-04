pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Deployment environment')
    }

    stages {

        stage('Print Environment') {
            steps {
                echo "Deploying to ${params.ENV}"
            }
        }

        stage('Deploy via SSH') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'remote-server',
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**/*',
                                    removePrefix: '',
                                    remoteDirectory: '/var/www/app',
                                    execCommand: ''
                                )
                            ]
                        )
                    ]
                )
            }
        }

        stage('Cleanup') {
            steps {
                cleanWs()
            }
        }
    }
}