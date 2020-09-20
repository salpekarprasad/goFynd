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


def test_Get_Newly_Created_Employee() :
    create_response = create_New_Employee("Fixtures/createEmployeeDetails.json")
    assert create_response.status_code == 200
    empl_id = parse("$.data.id")
    id = empl_id.find(create_response.json())

    get_employee_url = "http://dummy.restapiexample.com/api/v1/employee/"+str(id[0].value)

    get_response = requests.get(get_employee_url,
                       headers={"Accept": "*/*",
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
                                })
    assert get_response.status_code == 200

def test_Empty_UserAgent_Employee_Not_Created() :
    create_empty_employee = create_New_Employee("Fixtures/createEmployeeDetails.json",emptyUserAgent= True)
    # When no user agent is passed, server respond with 406 (Not Acceptable)
    assert create_empty_employee.status_code == 406




