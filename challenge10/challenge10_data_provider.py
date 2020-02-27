# https://www.dataquest.io/blog/python-api-tutorial/
# https://pypi.org/project/unittest-data-provider/
#Read test data from Excel sheet

import unittest
import requests
import json
import xlrd
from termcolor import colored
from ddt import ddt, data, unpack

def read_data():
    workbook = xlrd.open_workbook("TestDataExcel.xlsx")
    sheet = workbook.sheet_by_name("Employee")  # Read data from Excel sheet
    # Get number of rows with data in excel sheet
    row_count = sheet.nrows
    test_data = []
    for row in range(1,row_count):
        print(sheet.row_values(row))
        test_data.append(sheet.row_values(row))

    print(" Test data from Excel : {}".format(test_data))
    return test_data


@ddt
class Challenge10(unittest.TestCase):
    http_request = "http://dummy.restapiexample.com/api/v1/"

    def get_all_employee_details(self):
        print("In get_all_employee_details()")
        all_employee_req = self.http_request + "employees"
        resp = requests.get(all_employee_req, headers={"User-Agent": "XY"})
        print("Response code: {}".format(resp.status_code))
        response_dict = json.loads(resp.text)
        assert response_dict and (response_dict["status"] == "success"), "API call failed. Response code : {}".format(resp.status_code)
        return response_dict["data"]

    def get_employee_details(self, employee_id):
        print("In get_employee_details(employee_id)")
        employee_req = self.http_request + "employee/{}".format(employee_id)
        print(colored(employee_req, "green"))
        resp = requests.get(employee_req, headers={"User-Agent": "XY"})
        print("Response code: {}".format(resp.status_code))
        response_dict = json.loads(resp.text)
        assert response_dict and (response_dict["status"] == "success"), "Response data : {}".format(response_dict["data"])
        return response_dict["data"]

    def add_new_employee(self):
        print("In add_new_employee()")
        create_req = self.http_request + "create"
        print(colored(create_req, "green"))
        resp = requests.post(create_req, headers={"User-Agent": "XY"})
        print("Response code: {}".format(resp.status_code))
        response_dict = json.loads(resp.text)
        assert response_dict and (response_dict["status"] == "success"), "Response data : {}".format(response_dict["data"])
        return response_dict["data"]

    def update_employee_details(self, employee_id):
        print("In update_employee_details()")
        update_req = self.http_request + "update/{}".format(employee_id)
        print(colored(update_req, "green"))
        resp = requests.put(update_req, headers={"User-Agent": "XY"})
        print("Response code: {}".format(resp.status_code))
        response_dict = json.loads(resp.text)
        print(response_dict)
        assert response_dict and (response_dict["status"] == "success"), "Response data : {}".format(
            response_dict["data"])
        return response_dict["data"]

    def delete_employee(self, employee_id):
        print("In delete_employee()")
        delete_req = self.http_request + "delete/{}".format(employee_id)
        print(colored(delete_req, "green"))
        resp = requests.delete(delete_req, headers={"User-Agent": "XY"})
        print("Response code: {}".format(resp.status_code))
        response_dict = json.loads(resp.text)
        print(response_dict)
        assert response_dict and (response_dict["status"] == "success"), "Response data : {}".format(
            response_dict["message"])
        return response_dict["message"]

    @data(*read_data())
    @unpack
    def test_print_data_type_in_json_response(self, action, employee_id):
        if action == "list all":
            all_employees_list = self.get_all_employee_details()
            print(colored("All Employees", 'green'))
            for item in all_employees_list:
                print(item)

        elif action == "create":
            employee_details = self.add_new_employee()
            print(colored("New Employee Details", 'green'))
            print(employee_details)

        elif action == "update":
            employee_details = self.update_employee_details(int(employee_id))
            print("Updated Employee Details")
            print(employee_details)

        elif action == "delete":
            employee_details = self.delete_employee(int(employee_id))
            print("Deleted Employee Details")
            print(employee_details)

    if __name__ == '__main__':
        unittest.main()