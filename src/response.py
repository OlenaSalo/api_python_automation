import logging
import allure
from allure_commons.types import AttachmentType


class AssertableResponse(object):

    def __init__(self, response):
        allure.attach("Request  url = {} body = {}".format(response.request.url, response.request.body), "request.txt", AttachmentType.TEXT)
        logging.info("Request  url = {} body = {}".format(response.request.url, response.request.body))
        logging.info("Response status_code = {} body={}".format(response.status_code, response.text))
        self._response = response

    # @allure.step
    # def status_code(self, code):
    #     logging.info("Status code should be {}".format(code))
    #     return self._response.status_code == code
    #
    # @allure.step
    # def field(self, name):
    #     return self._response.json()[name]

    @allure.step('response should have {condition}')
    def should_have(self, condition):
        logging.info("About to check " + str(condition))
        condition.match(self._response)
        return self