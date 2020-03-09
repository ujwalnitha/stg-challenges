# https://www.dataquest.io/blog/python-api-tutorial/
# https://pypi.org/project/unittest-data-provider/
#Read test data from Excel sheet

import unittest
import requests
import json
from termcolor import colored


class Challenge9Dummy(unittest.TestCase):
    http_request = "http://dummy.restapiexample.com/api/v1/"

    def test_all_api(self):
        all_employee_req = self.http_request + "employees"
        resp = requests.get(all_employee_req, headers={"User-Agent": "XY"})
        print("Response code: {}".format(resp.status_code))
        response_dict = json.loads(resp.text)
        assert response_dict and (response_dict["status"] == "success"), "API call failed. Response code : {}".format(
            resp.status_code)
        print(response_dict["data"])

        url = "http://dummy.restapiexample.com/api/v1/update/7"
        response = requests.request("PUT", url, headers={"User-Agent": "XY"}, data={})
        print("****Response code: {}".format(response.status_code))
        print(response.request.headers)
        print(response.request.body)

        print(response.text.encode('utf8'))

        all_employee_req = self.http_request + "employees"
        resp = requests.get(all_employee_req, headers={"User-Agent": "XY"})
        print("Response code: {}".format(resp.status_code))
        response_dict = json.loads(resp.text)
        assert response_dict and (response_dict["status"] == "success"), "API call failed. Response code : {}".format(
            resp.status_code)
        print(response_dict["data"])

    if __name__ == '__main__':
        unittest.main()