# flask_errors_spike
This is a simple repo to show how we can use custom error classes and error handers to a flask app in order to get better error responses.  
Simply python3 app.py (need to have install flask) 
post request to `localhost:5000/login' with payload: {"username":"test", "password":"test123"} for a successful request. Remove a filed to get missing parameter error or set `active` variable to False to get Deactivated user error.
