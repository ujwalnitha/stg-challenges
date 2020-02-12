# https://www.dataquest.io/blog/python-api-tutorial/
# Find data type of response json elements

import unittest
import requests
import json
from termcolor import colored

class Challenge9(unittest.TestCase):

    def test_challenge9_api_json_data(self):
        search_tags = ["roku", "xbox", "iphone", "chrome"]
        for tag in search_tags:
            self.print_data_type_in_json_response(tag)

    @staticmethod
    def print_data_type_in_json_response(search_text = 'roku'):
        print("Search text : %s" % (search_text))
        resp = requests.get("https://help.sling.com/en/support/search.json?term=%s" % (search_text))
        print("resp.ok : {}".format(resp.ok))  # => True
        print("resp.status_code: {}".format(resp.status_code))  # => 200
        #print(json.dumps(resp.json(), sort_keys=True, indent=4))
        response_list = json.loads(resp.text)
        print(colored("Total search result for {} count: {}".format(search_text, len(response_list)), 'green'))
        for item in response_list:
            for key,val in item.items():
                print("{} : {}".format(key,type(val).__name__))

if __name__ == '__main__':
    unittest.main()