import requests
import json


def test_create_Empl() :
    req_body = {'name': 'kyle pogi',
                'salary': '3232323',
                'age': '34'}

    response = requests.post('http://dummy.restapiexample.com/api/v1/create', req_body)
    print(response.status_code)
    print(response.text)

    # id_exp = parse("$.id")
    # id = id_exp.find(response.json())
   # print (id[0].value)

def test_get_All_Empl() :

    get_all_employees = "http://dummy.restapiexample.com/api/v1/employees"
    res = requests.get(get_all_employees)
    assert res.status_code == 200

def test_Empl_by_Empl_No() :
    get_employee_by_EmpNo = "http://dummy.restapiexample.com/api/v1/employee/15"
    res = requests.get(get_employee_by_EmpNo)
    #assert res.status_code == 200