# How to Run Tests

* Import the project<br />
 `Use Pycharm to import the project`

* Install Pipenv <br />
 `pip install pipenv` <br />

* Install all dependencies from Pipfile<br />
 `pipenv install` <br />

* Run All Tests <br />
 `pipenv shell` <br />
 `pytest -v tests` <br />

# Problems in given API documentations

* The PUT API is not working as expected, I tried running the PUT API using POSTMAN, it shows success in the PUT Response.
But the Response data does not show the updated values,the response data continues to show the old values even after successful PUT request. <br />

*The Delete API is also not working as expected. The Response shows data is deleted successfully. But can retrieve the data using Id

* The APIs on domain - http://dummy.restapiexample.com/ keep failing with `HTTP error code 429`. This error happens because too many requests are sent to the APIs in a short time interval. 
This can be fixed by reading `Retry-After` response header. This header is not well implemented on this API which is why I could not integrate in my solution.
 