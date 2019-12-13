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

    def test_challenge2_not_using_contains(self):
        # Open Web page
        self.driver.get("https://www.copart.com/")

        # Search
        search_text_box = self.driver.find_element_by_xpath("//*[@id=\"input-search\"]")
        search_text_box.click()
        search_text_box.send_keys("exotics")
        search_text_box.send_keys(Keys.RETURN)

        # Verify if PORCHE is listed under model section
        wait = WebDriverWait(self.driver, 15)

        result_element = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@id=\"serverSideDataTable\"]//td//span[@data-uname=\"lotsearchLotmake\"]")))
        print("All lotsearchLotmake\n_____________________")
        for item in result_element:
            print(item.text)

        result_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable\"]")))
        print("Printing all result table" + result_element.text)

        # Assert for Text
        self.assertIn("PORSCHE", result_element.text)


if __name__ == '__main__':
    unittest.main()
