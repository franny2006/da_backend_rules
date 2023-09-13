node {
    def app

    try {

        stage('Clone repository') {
            /* Let's make sure we have the repository cloned to our workspace */

            checkout scm
        }

        stage('Build image') {
            try {
                sh 'docker stop da_backend_rules'
                }
            catch (Exception e) {
                echo 'Container stoppen nicht möglich:  ' + e.toString()
                }
            try {
                sh 'docker rm $(docker ps -a -q)'
                echo 'Gestoppte Container erfolgreich entfernt'
                }
            catch (Exception e) {
                echo 'Entfernen der gestoppten Container fehlgeschlagen'
                }
            sh 'docker-compose build'
        }

        stage('Start Containers') {
            sh 'docker-compose up -d'
          //  sh 'docker exec -i flaskdemo_db_1 mysql -h db -uroot -p"root" < /var/lib/jenkins/workspace/Flaskdemo/db/init.sql'
        }

    //    stage('Export Cucumber') {
    //        step([$class: 'XrayExportBuilder', filePath: '/var/lib/jenkins/workspace/Demoanwendung_Backend/app/features', issues: 'DB-12;DB-17', serverInstance: '8cad2d10-c6a7-43ca-8dc5-9bdbd7ae8eec'])
    //    }

        stage('Execute Testsets') {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                sh 'cd /var/lib/jenkins/workspace/Demoanwendung_Backend/app'
                dir('app'){
                    echo "Workdir=$WORKSPACE"
                    sh 'ls -l'
                    dir ('testreports') {
                        writeFile file:'dummy', text:''
                        }
                    sh 'ls -l'
                    // sh 'behave  --junit --junit-directory /var/lib/jenkins/workspace/Demoanwendung_Backend/app/testreports'
                    sh 'behave -f json -o /var/lib/jenkins/workspace/Demoanwendung_Backend/app/reports/behave_report.json'
                    }
            }
        }

        stage('Create Network Connectivity') {
            sh 'docker network prune'
            sh 'docker network connect demoNetz da_backend_rules'
          //  sh 'docker exec -i flaskdemo_db_1 mysql -h db -uroot -p"root" < /var/lib/jenkins/workspace/Flaskdemo/db/init.sql'
        }


       stage('Import results to Xray and Jenkins') {
            junit '**/testreports/*.xml'
       //     sh 'cd /var/lib/jenkins/workspace/Demoanwendung_Backend/app'
       //     sh 'python3 -m behave2cucumber -i /var/lib/jenkins/workspace/Demoanwendung_Backend/app/reports/behave_report.json -o /var/lib/jenkins/workspace/Demoanwendung_Backend/app/reports/cucumber_json.json'
       //   letzte Version: step([$class: 'XrayImportBuilder', endpointName: '/junit', importFilePath: '/var/lib/jenkins/workspace/Demoanwendung_Backend/app/testreports/*.xml', importToSameExecution: 'true', projectKey: 'DB', serverInstance: '8cad2d10-c6a7-43ca-8dc5-9bdbd7ae8eec'])
       //     step([$class: 'XrayImportBuilder', endpointName: '/cucumber', importFilePath: '/var/lib/jenkins/workspace/Demoanwendung_Backend/app/reports/cucumber_json.json', importToSameExecution: 'true', projectKey: 'DB', serverInstance: '8cad2d10-c6a7-43ca-8dc5-9bdbd7ae8eec'])
       }
   }
   catch (e) {
        echo "Fehlerhafter Build"
        throw e
   }

   finally {
        publishTestResults serverAddress: 'https://testmanufaktur.atlassian.net',
            projectKey: 'DA',
            format: 'Json',
            filePath: '**/reports/*.json',
            autoCreateTestCases: true,
              customTestCycle: [
                name: 'Jenkins Build',
                description: 'Results from Jenkins Build',
                jiraProjectVersion: '10001',
                folderId: '3040527',
                customFields: '{"number":50,"single-choice":"option1","checkbox":true,"userpicker":"5f8b5cf2ddfdcb0b8d1028bb","single-line":"a text line","datepicker":"2020-01-25","decimal":10.55,"multi-choice":["choice1","choice3"],"multi-line":"first line<br />second line"}'
              ]
   }

}