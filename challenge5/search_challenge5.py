import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SearchChallenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        # Open Web page
        self.driver.get("https://www.copart.com/")
        self.driver.maximize_window()

        # Search
        search_text_box = self.driver.find_element_by_xpath("//*[@id=\"input-search\"]")
        search_text_box.click()
        search_text_box.send_keys("porsche")
        search_text_box.send_keys(Keys.RETURN)

        # Wait for search result to load
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "// *[@id=\"serverSideDataTable\"]//tbody//tr")))

        # Select 100 from drop down
        drop_down_element = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id=\"serverSideDataTable_length\"]/label/select/option[@value=\"100\"]")))
        drop_down_element.click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable_processing\"][contains(@style, 'display: none')]")))

        # Find all models
        result_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-uname=\"lotsearchLotmodel\"]")))
        # Get frequency count of duplicate models and add to dictionary
        dict_model_count = dict()
        for item in result_element:
            model = item.text
            if model:
                # If element exists in dict then increment its value else add it in dict
                if model in dict_model_count:
                    dict_model_count[model] += 1
                else:
                    dict_model_count[model] = 1
        print("------------------------------------------------")
        print(" %s different models in result page" % (len(dict_model_count)))
        print('{:<15s}:{:>6s}'.format("Model", "Count"))
        print("............................")
        for model, count in dict_model_count.items():
            print('{:<15s}:{:>4s}'.format(str(model), str(count)))

        # Count Damage types : Get all Damages list
        damages_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@data-uname=\"lotsearchLotdamagedescription\"]")))
        # Get frequency count of duplicate models and add to dictionary
        dict_damages_count = {"MINOR DENT/SCRATCHES": 0, "REAR END": 0, "FRONT END": 0, "UNDERCARRIAGE": 0, "MISC": 0}
        # Iterate over each element in list
        for item in damages_elements:
            damage = item.text
            if damage:
                # If element exists in dict then increment its value else add it in dict
                if damage in dict_damages_count:
                    dict_damages_count[damage] += 1
                else:
                    dict_damages_count["MISC"] += 1
        print("------------------------------------------------")
        print('{:<25s}:{:>6s}'.format("Damage", "Count"))
        print("............................")
        for damage, count in dict_damages_count.items():
            print('{:<25s}:{:>4s}'.format(str(damage), str(count)))


if __name__ == '__main__':
    unittest.main()
