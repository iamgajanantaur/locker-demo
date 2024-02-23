pipeline {
    agent any
    stages {    
        stage ('docker image build') {
            steps {
                sh '/usr/bin/docker build -t iamgajanantaur/locker-allocation:latest .'    
            }
        }
        
        stage ('docker login') {
            steps {
                sh 'echo dckr_pat_-QY9vlD8nsvi0Mvp7wFIk9CdcXc | /usr/bin/docker login -u iamgajanantaur --password-stdin'
            }
        }
        
        stage ('docker push') {
            
            steps {
                sh '/usr/bin/docker image push iamgajanantaur/locker-allocation:latest'
            }
        }
        
        
        stage ('existings service remove') {
            steps {
                sh '/usr/bin/docker service rm locker-con'
            }
        }
        
        stage ('start sevice') {
            steps {
                sh '/usr/bin/docker service create --name locker-con -p 80:5000 --replicas 2 iamgajanantaur/locker-allocation'
            }
        }
        
        
    }
    
}

