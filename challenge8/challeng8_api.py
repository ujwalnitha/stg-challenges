# api testing reference : https://chercher.tech/python/api-testing-selenium-python
# http://www.compjour.org/tutorials/intro-to-python-requests-and-json/
# This test is to search for different models and get total results count to a text file
# Using API testing, not from UI
import json
import unittest
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge8(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge8_api(self):
        self.search_using_api("porsche")

    @staticmethod
    def search_using_api(self, search_text=""):
        resp = requests.get("https://help.sling.com/en/support/search?term={}".format(search_text))
        #resp = requests.get("https://www.copart.com/lotSearchResults/?free=true&query={}".format(search_text))
        print("resp.ok : {}".format(resp.ok))  # => True
        print("resp.status_code: {}".format(resp.status_code))  # => 200
        print("resp.headers['content-type'] : {}".format(resp.headers['content-type']))  # => "text/html"
        print("resp.text : \n {}".format(resp.text))


if __name__ == '__main__':
    unittest.main()