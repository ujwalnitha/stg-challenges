import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_login(self):

        # Open URL
        self.driver.get("https://watch.sling.com")

        # Wait until Login page is loaded
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Enter Email, Password and Sign In
        self.driver.find_element_by_name('email').send_keys("xxxxxxxx")
        self.driver.find_element_by_name('password').send_keys("11111")
        self.driver.find_element_by_class_name("sign-in-up-button-container").click()

        # Wait for Landing page
        wait.until(EC.title_contains("MY TV"))
        print("Title is : %s " % self.driver.title)
        time.sleep(10)  # Not a good practice: still waiting to View the Landing page manually


if __name__ == '__main__':
    unittest.main()
