import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://watch.sling.com")
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.title_contains("MY TV"))
        print("Title is : %s " %(self.driver.title))


if __name__ == '__main__':
    unittest.main()
