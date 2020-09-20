import requests
import json
from jsonpath_ng import parse
import time
from fake_useragent import UserAgent


def create_New_Employee(fixturefilepath) :
    headers = {"Content-Type": "application/json", "Accept": "*/*","Content-Length": "42", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    f = open(fixturefilepath, "r")
    create_request = json.loads(f.read())
    return requests.post("http://dummy.restapiexample.com/api/v1/create", create_request,headers=headers)

def get_Employee(empId,emptyUserAgent = False) :
    base_url = "http://dummy.restapiexample.com/api/v1/employee/"
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    print(user_agent)
    header = {"Content-Type": "application/json", "Accept": "*/*"}
    if emptyUserAgent == False :
        header.update(user_agent)

    get_employee_url = base_url if empId == None else base_url+empId
    return requests.get(get_employee_url,headers=header)

def delete_Employee(empId,emptyUserAgent = False) :
    base_url = "http://dummy.restapiexample.com/api/v1/delete/"
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    print(user_agent)
    header = {"Content-Type": "application/json", "Accept": "*/*"}
    if emptyUserAgent == False:
        header.update(user_agent)

    delete_employee_url = base_url if empId == None else base_url+empId
    return requests.delete(delete_employee_url,headers = header)

def test_Delete_Newly_Created_Employee() :
    time.sleep(1)
    create_response = create_New_Employee("Fixtures/createEmployeeDetails.json")
    assert create_response.status_code == 200
    empl_id = parse("$.data.id")
    id = empl_id.find(create_response.json())

    get_response_before_delete = get_Employee(str(id[0].value))
    assert get_response_before_delete.status_code == 200

    delete_response = delete_Employee(str(id[0].value))
    assert delete_response.status_code == 200

    get_response_after_delete = get_Employee(str(id[0].value))
    assert get_response_after_delete.status_code == 200






