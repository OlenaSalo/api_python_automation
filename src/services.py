import json
import os
import allure

import requests
from requests import Session

from src.response import AssertableResponse


class ApiService(object):

    def __init__(self):
        self.session = Session()
        self._base_url = os.environ['BASE_URL']
        self._headers = {"content-type": "application/json"}

    def post(self, url,  body):
        # self._headers = {}
        return requests.post("{}{}".format(self._base_url, url), data=json.dumps(body),
                      headers = self._headers)

    # def auth(self):
    #     return requests.post("").json()["token"]

class UserApiService(ApiService):

    def __init__(self):
        super().__init__()


    @allure.step
    def create_user(self, user):


        return AssertableResponse(self.post("/register", user))