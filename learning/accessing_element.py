
# This is a simple practice code to send access an element and get properties
# __author__ = Nitha Ujwal

import unittest
from selenium import webdriver


class ElementAccess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_accessing_simple_elements(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        print("Python found in Title")
        element = driver.find_element_by_id("id-search-field")
        print("Element Type (Tag name): %s" % element.tag_name)
        element = driver.find_element_by_name("q")
        print("Element Text (text): %s" % element.get_property("name"))
        element = driver.find_element_by_class_name("search-field")
        print("Element Text (text): %s" % element.get_property("id"))
        element = driver.find_element_by_xpath("//input[@name='q']")
        print("Element Text (text): %s" % element.get_property("placeholder"))


if __name__ == '__main__':
    unittest.main()
