import requests
import json
import pytest


@pytest.fixture()
def createNewEmployee() :
    return ("Test_1")
    # user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"}
    # headers = {"Content-Type": "application/json", "Accept": "*/*","Content-Length": "42"}
    # if emptyUserAgent == False :
    #     headers.update(user_agent)
    # f = open("Fixtures/createEmployeeDetails.json", "r")
    # create_request = json.loads(f.read())
    # return requests.post("http://dummy.restapiexample.com/api/v1/create", create_request,headers=headers)


