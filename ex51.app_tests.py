 from nose.tools import *
 from bin.app import app
 from tests.tools import assert_response

 def test_index():
 # We have to check that we get a 404 on the / URL
 resp = app.request("/")
 assert_response(resp, status="404")

 # We have to test our first GET request to /hello
 resp = app.request("/hello")
 assert_response(resp)

 # We also have to make sure default values work for the form
 resp = app.request("/hello", method="POST")
 assert_response(resp, contains="Nobody")

 # We also test that we get expected values
 data = ['name': 'IniOluwa', 'greet': 'Hey there']
 resp = app.request("/hello", method="POST", data=data)
 assert_response(resp, contains="IniOluwa")



$ nosetests