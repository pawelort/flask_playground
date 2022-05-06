from flask import Flask

app = Flask('first app')

@app.route('/')
def hello_display():
    return 'hello world!'

@app.route('/about')
def blabla():
    return 'this will have some information in the future'

app.run()