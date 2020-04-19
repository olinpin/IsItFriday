from flask import Flask, render_template
import datetime


app = Flask(__name__)

@app.route("/")
def isfriday():
    now = datetime.datetime.now()
    WeekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    friday = now.weekday() == 4
    return render_template("index.html", friday=friday)
    