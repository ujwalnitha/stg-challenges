'''
Search for a rare model, Handle exception if the search result is empty.
Capture screen shot in Error handling code
'''


#import traceback
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExceptionChallenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        # Open Web page
        self.driver.get("https://www.copart.com/")
        self.driver.maximize_window()

        # Search for 'nissan'
        search_text_box = self.driver.find_element_by_xpath("//*[@id=\"input-search\"]")
        search_text_box.click()
        search_text_box.send_keys("nissan")
        search_text_box.send_keys(Keys.RETURN)

        # Wait for search result to load and click on Model Filter
        wait = WebDriverWait(self.driver, 15)
        model_filter_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-uname=\"ModelFilter\"]")))
        model_filter_element.click()

        # Search for a rare model
        search_text = "Patrol"
        search_model_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class =\"list-group-item more\"]//input[@placeholder=\"Search\"]")))
        search_model_element.send_keys(search_text)

        try:
            # Check for results
            results_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@class =\"list-group-item more\"]//*[@class=\"checkbox\"]//label")))
            for item in results_elements:
                print(item.text)
                assert search_text in item.text, "Model filter showing wrong options"

        except TimeoutException:
            print("No search result, capturing screen shot")
            # traceback.print_exc()     # If detailed stack trace is required
            timestamp = str(time.time()).split('.')[0]
            self.driver.save_screenshot("./ErrorScreenshots/search_no_result%s.png" %(timestamp))


if __name__ == '__main__':
    unittest.main()
