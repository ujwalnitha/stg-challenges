import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Challenge3LoopSlingSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_loop_sling_search(self):
        # Open Web page
        self.driver.get("https://help.sling.com")
        self.driver.maximize_window()

        # Initialize
        wait = WebDriverWait(self.driver, 15)
        search_input = 'roku'

        # Wait until 'Search' is loaded, and search for search_input
        search_input_element = wait.until(ec.presence_of_element_located((By.ID, "support-search-input")))
        search_input_element.send_keys(search_input)
        search_input_element.send_keys(Keys.RETURN)

        # Find all elements under tag search-results-list->a
        all_result_elements = self.driver.find_elements_by_xpath("//*[@class=\"search-results-list\"]//a")
        count_search_word = 0
        # Print all items and href, and get count of search word in search result
        for item in all_result_elements:
            search_result_text = item.text
            if search_input in search_result_text.lower():
                count_search_word += 1
            print(" " + search_result_text + ": " + item.get_property("href"))

        # Verify that Search word appears at least once in search result
        print("-------------------------\n%s appears %d times in Search result" % (search_input, count_search_word))
        assert count_search_word, "%s appears %d times in Search result" % (search_input, count_search_word)


if __name__ == '__main__':
    unittest.main()
