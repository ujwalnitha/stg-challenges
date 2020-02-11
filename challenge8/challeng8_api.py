# api testing reference : https://chercher.tech/python/api-testing-selenium-python
# http://www.compjour.org/tutorials/intro-to-python-requests-and-json/
# This test is to sling help search and get total results count
# Response will be written to a text file, response.txt at current location
# Using API testing, not from UI

import unittest
import requests
import json
from selenium import webdriver
from termcolor import colored

class Challenge8(unittest.TestCase):

    def test_challenge8_api(self):
        self.search_using_api("xbox")

    @staticmethod
    def search_using_api(search_text="roku"):
        print("Search text : %s" %(search_text))
        resp = requests.get("https://help.sling.com/en/support/search.json?term=%s"%(search_text))
        print("resp.ok : {}".format(resp.ok))  # => True
        print("resp.status_code: {}".format(resp.status_code))  # => 200
        file = open("response.txt", "w")
        file.write(resp.text)
        file.close()
        response_dict = json.loads(resp.text)
        #Print search result titles
        for item in response_dict:
            print(item["title"])
        print(colored("Total search result count: {}".format(len(response_dict)), 'green'))

if __name__ == '__main__':
    unittest.main()
