node {
       stage('Checkout repo') {
               git branch: 'main',
                url: "https://github.com/OlenaSalo/api_python_automation.git"
              }

          stage("Install deps"){
            sh 'pipenv install'
          }

          stage('Test'){
            sh 'pipenv run pytest tests -sv --alluredir=allure_results'
          }

          stage("Report"){
           allure([
                        includeProperties: false,
                        jdk: '',
                        properties: [],
                        reportBuildPolicy: 'ALWAYS',
                        results: [[path: 'allure_results']]
                    ])
          }
     }

//                 agent {
//                     docker {
//                         image '3.10'
//                     }
//                 }
//
//             steps{
//                 git branch: 'main',
//                 url: "https://github.com/OlenaSalo/api_python_automation.git"
//                 sh """
//                  pipenv install
//                  pipenv run pytest tests -sv --alluredir=allure_results
//                 """
//                 allure([
//                         includeProperties: false,
//                         jdk: '',
//                         properties: [],
//                         reportBuildPolicy: 'ALWAYS',
//                         results: [[path: 'allure_results']]
//                     ])
//                 sh 'pipenv install'
//                 sh 'pipenv run pytest tests -sv --alluredir=allure_results'