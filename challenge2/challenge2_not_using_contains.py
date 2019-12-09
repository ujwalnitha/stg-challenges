import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        self.driver.find_element_by_id('input-search').click()
        self.driver.find_element_by_id('input-search').send_keys("exotics")
        self.driver.find_element_by_xpath("//button[contains(.,'Search')]").click()

        # Verify if PORCHE is listed under model section
        wait = WebDriverWait(self.driver, 15)

        result_element = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@id=\"serverSideDataTable\"]//td//span[@data-uname=\"lotsearchLotmake\"]")))
        for item in result_element:
            print("Printing all elements with property lotsearchLotmake " + item.text)

        result_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[@id=\"serverSideDataTable\"]")))
        print("Printing all result table" + result_element.text)
        self.assertIn("PORSCHE", result_element.text)
        

if __name__ == '__main__':
    unittest.main()
