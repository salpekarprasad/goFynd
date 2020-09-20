# The API is not working as expected, I tried running the PUT API using POSTMAN, it shows success in the PUT Response
# But the Response data dose not show the updated values,
# the response data continues to show the old values even after successful PUT request


import requests
import json
from jsonpath_ng import parse


def create_New_Employee(fixturefilepath,emptyUserAgent = False) :

    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    headers = {"Content-Type": "application/json", "Accept": "*/*","Content-Length": "42"}
    if emptyUserAgent == False :
        headers.update(user_agent)
    f = open(fixturefilepath, "r")
    create_request = json.loads(f.read())
    return requests.post("http://dummy.restapiexample.com/api/v1/create", create_request,headers=headers)


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
    update_request = json.loads(f.read())
    return requests.put(update_employee_url,update_request,headers = header)

def test_Update_Existing_Employee_Details():
    create_response = create_New_Employee("Fixtures/createEmployeeDetails.json")
    assert create_response.status_code == 200
    empl_id = parse("$.data.id")
    id = empl_id.find(create_response.json())

    get_response_before_update = get_Employee(str(id[0].value))
    assert get_response_before_update.status_code == 200

    update_response = update_Employee("Fixtures/updateEmployeeDetails.json",str(id[0].value))
    assert  update_response.status_code == 200

    get_response_after_update_before_delete = get_Employee(str(id[0].value))
    assert get_response_after_update_before_delete.status_code == 200







