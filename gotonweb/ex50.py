# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     greeting = "World"
#     return f'Hello, {greeting}'

# if __name__ == "__main__":
#     app.run()

##-------------v2

# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route("/") # when there is a request / ends in / flask will go to def index
# def index():
#     greeting = "Hello World"
#     return render_template("web_form.html", greeting=greeting)

# if __name__ == "__main__":
#     app.run()

##-------------v3 with web_form.py

# 1) cd E:\python_work\Meat_shop\gotonweb
# 2) python ex50.py
# 3) Browser: http://127.0.0.1:5000/hello => action="/hello" -- pulls up web_form.html
# 4) Method POST can/receives values for var.s name & greet => if request.method == True:
# 5) return render_template("index.html") => I just wanted to say 'greet' 'name'

from flask import Flask
from flask import render_template
from flask import request

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

if __name__ == "__main__":
    app.run()

