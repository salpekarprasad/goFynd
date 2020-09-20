# The API is not working as expected, I tried running the API using POSTMAN, IT shows success in PUT request but when
# we try to GET the same record it show the old data and not the updated one


import requests
import json
from jsonpath_ng import parse
import time
from fake_useragent import UserAgent



def get_Employee(empId,emptyUserAgent = False):
    base_url = "http://dummy.restapiexample.com/api/v1/employee/"
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    print(user_agent)
    header = {"Content-Type": "application/json", "Accept": "*/*"}
    if emptyUserAgent == False :
        header.update(user_agent)

    get_employee_url = base_url if empId == None else base_url+empId
    return requests.get(get_employee_url,headers=header)


def update_Employee(fixturefilepath,empId,emptyUserAgent = False) :
    base_url = "http://dummy.restapiexample.com/api/v1/update/"
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    header = {"Content-Type": "application/json", "Accept": "*/*"}
    if emptyUserAgent == False:
        header.update(user_agent)

    update_employee_url = base_url if empId == None else base_url + empId
    f = open(fixturefilepath, "r")
    create_request = json.loads(f.read())
    return requests.put(update_employee_url,create_request,headers = header)

def test_Update_Existing_Employee_Details():
    time.sleep(1)

    get_response_before_update = get_Employee(str(id[0].value))
    assert get_response_before_update.status_code == 200

    update_response = update_Employee("Fixtures/updateEmployeeDetails.json",str(id[0].value))
    assert  update_response.status_code == 200

    get_response_after_update_before_delete = get_Employee(str(id[0].value))
    assert get_response_after_update_before_delete.status_code == 200







