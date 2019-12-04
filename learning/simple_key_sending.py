
# This is a simple practice code to send keys on an element
# __author__ = Nitha Ujwal

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SimpleKeySending(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_simple_key_sending(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        print("Python found in Title")
        element = driver.find_element_by_id("id-search-field")
        element.clear()
        element.send_keys("pycon")
        print("Searching for pycon")
        element.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        print("Search succeeded")


if __name__ == '__main__':
    unittest.main()
