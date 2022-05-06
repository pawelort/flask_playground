from flask import Flask, make_response
import datetime

app = Flask('main')

@app.route('/')
def main_view():
    time = datetime.datetime.now()
    year, month, day = time.year, time.month, time.day

    return make_response(time.strftime('%Y.%m.%d'), 200)
    # return make_response(f"{year}.{month}.{day}", 200)

app.run()