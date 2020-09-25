
import requests
import json
import pytest
import pytest



@pytest.mark.usefixtures("createNewEmployee")
class TestCreateEmployee:


    def test_Get_Newly_Created_Employee(self, createNewEmployee):
        print(createNewEmployee)
        # empl_id = parse("$.data.id")
        # id = empl_id.find(create_response.json())
        #
        # get_employee_url = "http://dummy.restapiexample.com/api/v1/employee/" + str(id[0].value)
        #
        # get_response = requests.get(get_employee_url,
        #                             headers={"Accept": "*/*",
        #                                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        #                                      })
        # assert get_response.status_code == 200


