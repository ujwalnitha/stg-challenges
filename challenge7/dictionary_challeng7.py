import re
import json
import unittest
import requests

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Challenge6ValidateURLs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge7_dictionary(self):
        # Open Web page
        self.driver.get("https://www.copart.com/")

        # Verify if Popular Searches is loaded
        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Trending")))

        # Find all elements under tag popular searches->a
        all_trending_elements = self.driver.find_elements_by_xpath("//*[@ng-if=\"popularSearches\"]//a")
        # Add all items and href to dictionary and print
        model_link_dict = {}
        for item in all_trending_elements:
            model = item.text
            url = item.get_property("href")
            model_link_dict[model] = url

        # Print contents of dict in json like format
        print(json.dumps(model_link_dict, indent=4))

        # Verify if each URL is valid
        for model, url in model_link_dict.items():
            model = str(model).lower().replace(" ", "-")
            assert re.search('https://www.copart.com/popular/(?:[make]|[model])+/%s' % model, url), "URL format is incorrect"

            # Verify each URL opens correct page, *******certificate issue occurs
            try:
                print(requests.head(url).status_code)
            except Exception as e:
                print(e.args)


if __name__ == '__main__':
    unittest.main()
