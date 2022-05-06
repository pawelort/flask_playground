from flask import Flask

app = Flask('first_proj')

@app.route("/")
def welcome():
    return "Welcome to my Flash Cards application!"

