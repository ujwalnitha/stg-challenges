import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class challenge2_copart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2_copart(self):
        # Open Web page
        self.driver.get("https://www.copart.com/")

        # Search
        search_text_box = self.driver.find_elements_by_xpath("//*[@id=\"input-search\"]")
        search_text_box.click()
        search_text_box.send_keys("exotics")
        search_text_box.send_keys(Keys.RETURN)

        # Verify if PORSCHE is listed under model section
        wait = WebDriverWait(self.driver, 15)
        result_span_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(.,'PORSCHE')]")))
        text_found = result_span_element.text
        print("Search result with PORSCHE text: %s" % text_found)
        self.assertEqual('PORSCHE', text_found, "Failed to find PORSCHE in Search Result")


if __name__ == '__main__':
    unittest.main()
