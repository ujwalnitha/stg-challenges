import unittest
from challenge5.AltFinder import *
from selenium import webdriver
from termcolor import colored

class AltFindChallenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_alt_find(self):
        # Open Web page
        self.driver.get("https://www.sling.com/")
        self.driver.maximize_window()
        tags_with_alt = ["area", "img", "input"]

        for tag in tags_with_alt:
            # Create AltFinder object for each tag
            elements_obj = MyAltFinder(self.driver, tag)
            elements_with_alt = elements_obj.get_all_elements_with_alt()
            if elements_with_alt:
                print(colored("*******************************\n<%s> elements in this page with alt attribute" % elements_obj.tag, "green"))
                self.print_elements(elements_with_alt, alt=True)
            elements_without_alt = elements_obj.get_all_elements_without_alt()
            if elements_without_alt:
                print(colored("********************************\n<%s> elements in this page without alt attribute" % elements_obj.tag, "red"))
                self.print_elements(elements_without_alt, alt=False)


    def print_elements(self, elements_list, alt = False):
        empty_alt_count = 0
        if alt:
            for (count, element) in enumerate(elements_list):
                alt_value = element.get_property("alt")
                source_value = element.get_property("src")
                if not alt_value:
                    empty_alt_count += 1
                    alt_value = colored("This alt attribute has no value", 'red')
                print("%d : %s - %s" % (count, source_value, alt_value))
            if empty_alt_count:
                print(colored("There are %d tags with empty alt attribute" % empty_alt_count, 'red'))

        else:
            for count,element in enumerate(elements_list):
                print("%d : %s %s %s" % (count, element.get_property("value"), element.text, element.tag_name))


if __name__ == '__main__':
    unittest.main()
