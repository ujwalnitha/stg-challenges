import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Challenge3Loop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_loop(self):
        # Open Web page
        self.driver.get("https://www.copart.com/")

        # Verify if Popular Searches is loaded
        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Trending")))

        # Find all elements under tag tabTrending->a
        all_trending_elements = self.driver.find_elements_by_xpath("//*[@id=\"tabTrending\"]//a")
        # Print all items and href
        for item in all_trending_elements:
            print(" " + item.text + ": " + item.get_property("href"))


if __name__ == '__main__':
    unittest.main()
