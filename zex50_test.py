# test target Meat_store_flask.py in C:\Users\I5\Desktop\python_work\Meat_store_online

# https://www.geeksforgeeks.org/python-import-module-outside-directory/
# sys.path variable of the module sys contains the list of all directories in which python will search for a module to import
# IMPORT MODULE FROM DIFFERENT DIRECTORY
# A)
# import sys # replaced: from app import app # with import sys & import Meat_store_flask
# sys.path.insert(1, 'C:/Users/I5/Desktop/python_work/Meat_store_online') # changed: \ to /
# #sys.path.append('C:\Users\I5\Desktop\python_work\Meat_store_online')
# import Meat_store_flask
# # Meat_store_flask.hello() # called & used function -- WORKED

# B) solved h2 import module from different direct via sys module
import sys
sys.path.insert(1, 'C:/Users/I5/Desktop/python_work/Meat_shop')
#import ex50 # instead of import ex50 I just copied it here to get it to work

# Rather than importing ex50, I simply copied it in
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/hello", methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST": 
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("web_form.html")

# copilot adapted the code from nose to pytest & it works / passes checks
import pytest

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True) # https://www.w3schools.com/PYTHON/ref_requests_get.asp
# get() method sends a GET request to the specified url
# SYNTAX: x = requests.get('url', params={key: value}, args) 
    assert rv.status_code == 404 # returns 404 since page doesn't exist

    rv = web.get('/hello', follow_redirects=True)
    assert rv.status_code == 200 # check /hello works with both a GET & POST form
    assert b"Fill Out This Form" in rv.data
# 'b' character b4 a string specifies string as "byte string" <=> python interprets as sequence of bytes rather than characters
# bytes literals are used to represent binary data like encoded text, pictures, audio, other data

    data = {'name': 'Zed', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data) # using post() M., send a POST request
# then give post() the data in the form as a dict ; data = {'name': 'Zed', 'greet': 'Hola'}
    assert b"Zed" in rv.data 
    assert b"Hola" in rv.data

if __name__ == "__main__":
    pytest.main()



