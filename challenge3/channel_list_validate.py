import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Challenge3ChannelListValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_channel_list_validation(self):
        # Open Web page
        self.driver.get("https://sling.com")

        # Initialize wait
        wait = WebDriverWait(self.driver, 15)

        # Verify if the Orange Tab is selected
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id=\"planOne\"][contains(@class, 'active-tab')]")))

        # Get Orange channel details
        orange_channel_details = self.get_channel_details()
        print("Orange package has %d channels " % (len(orange_channel_details)))

        # Select Blue package
        blue_tab_element = self.driver.find_element(By.ID, "planTwo")
        blue_tab_element.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id=\"planTwo\"][contains(@class, 'active-tab')]")))

        # Get Blue channel details
        blue_channel_details = self.get_channel_details()
        print("Blue package has %d channels " % (len(blue_channel_details)))

        # Select Orange & Blue package
        orange_and_blue_tab_element = self.driver.find_element(By.ID, "planThree")
        orange_and_blue_tab_element.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id=\"planThree\"][contains(@class, 'active-tab')]")))

        # Get Orange & Blue package details
        orange_and_blue_channel_details = self.get_channel_details()
        print("Orange & Blue package has %d channels " % (len(orange_and_blue_channel_details)))

        # Merge Orange Channel list and Blue channel List
        orange_plus_blue_details = orange_channel_details.copy()
        orange_plus_blue_details.update(blue_channel_details)
        print("Orange and Blue packages when combined has %d channels " % (len(orange_plus_blue_details)))

        # Check if Orange & Blue package shows correct number of channels
        assert len(orange_and_blue_channel_details) == len(orange_plus_blue_details), "Orange & Blue package channels count does not match with sum of dictinct Orange package channels and Blue package channels"
        assert all(channel in orange_and_blue_channel_details for channel in orange_plus_blue_details), "Channels in Orange & Blue package do not match with Orange package and Blue packages combined"

    def get_channel_details(self):
        # Initialize wait
        wait = WebDriverWait(self.driver, 15)

        # Find all elements under tag images from channel list
        time.sleep(5)  # Taking time to load all channel icons
        all_orange_channels = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//*[@id=\"channelList\"]//img")))
        channel_details_dict = {}
        # Get all items and href
        for item in all_orange_channels:
            channel_name = item.get_property("alt")
            channel_image = item.get_property("src")
            print(" " + channel_name + ": " + channel_image)
            channel_details_dict[channel_name] = channel_image
        return channel_details_dict


if __name__ == '__main__':
    unittest.main()
