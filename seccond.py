pipeline {
    agent any
    tools{
        maven 'maven_3_5_0'
    }
    stages{
        stage("Maven build"){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Chandupoorna472/devops_CICD']]])
                bat 'mvn clean install'
            }
        }
       
       
    }
}