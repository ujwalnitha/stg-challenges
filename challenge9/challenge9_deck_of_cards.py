# https://www.dataquest.io/blog/python-api-tutorial/
# Find data type of response json elements
# Validate type of some response elements

import unittest
import requests
import json
from termcolor import colored

class Challenge9_2(unittest.TestCase):

    def test_challenge9_api_json_data_2(self):
        for count in range(1,5):
            self.print_deck_details(count)

    @staticmethod
    def print_deck_details(deck_count = 1):
        resp = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=%s" % (deck_count))
        print("resp.ok : {}".format(resp.ok))  # => True
        print("resp.status_code: {}".format(resp.status_code))  # => 200
        print(json.dumps(resp.json(), sort_keys=True, indent=4))
        response_list = json.loads(resp.text)
        print(colored("Total search result for {} count: {}".format(deck_count, len(response_list)), 'green'))
        for key, val in response_list.items():
            print("{} : {}".format(key, type(val).__name__))
            if key == 'deck_id':
                assert isinstance(val, str), " Value of '{}' is not expected type".format(key)
            elif key == 'remaining':
                assert isinstance(val, int), " Value of '{}' is not expected type".format(key)
            elif key == 'shuffled' or key == 'success':
                assert isinstance(val, bool), " Value of '{}' is not expected type".format(key)

    if __name__ == '__main__':
        unittest.main()