node {

   stage('Build') {
            agent {
                docker {
                    image '3.11.3-alpine3.17'
                }
            }

  stage("Checkout repo"){
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
  script {
  allure(
  includeProperties: false,
  jdk: '',
  properties: [],
  reportBuildPolice: 'ALWAYS',
  result: [[path: 'allure_results']]
  )}
  }
}