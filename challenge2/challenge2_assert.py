import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class challenge2_assert(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2_assert(self):

        # Open URL
        self.driver.get("https://watch.sling.com")

        # Wait until Login page is loaded
        wait = WebDriverWait(self.driver, 15)
        email_element = wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Enter Email, Password and Sign In
        email_element.send_keys("xxxxxx")
        self.driver.find_element_by_name('password').send_keys("11111")
        self.driver.find_element_by_class_name("sign-in-up-button-container").click()

        # Wait for Landing page
        wait.until(EC.title_contains("MY TV"))
        print("Title is : %s " % self.driver.title)

        # Navigate to Search and type 'football'
        search_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".SearchInputstyled__NavSearchButton-ielYJJ")))
        search_element.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".dropdown-item-left")))
        self.driver.find_element_by_id("searchInput").send_keys("football")

        # Assert Top Result as active tab and populated
        search_result_active_tab = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".active-tab")))
        print("Search result active tab is : %s " % search_result_active_tab.text)
        self.assertIn("TOP RESULTS", search_result_active_tab.text)

        # Assert if search text is found in the first result
        first_tile_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tile-container:nth-child(1) .meta-title")))
        print("Search result first tile meta title is : %s " % first_tile_title.text)
        self.assertIn('football', first_tile_title.text.lower())


if __name__ == '__main__':
    unittest.main()
