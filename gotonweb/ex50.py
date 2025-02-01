# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     greeting = "World"
#     return f'Hello, {greeting}'

# if __name__ == "__main__":
#     app.run()

##-------------v2

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/") # when there is a request / ends in / flask will go to def index
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()