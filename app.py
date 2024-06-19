from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    return redirect('https://calendar.google.com/calendar/appointments/schedules/AcZssZ2sk3NFyxU_bm5QwFzEXLEhaZ-QyLJdYGxEqaSQCEOvBejRuBwE6fmxcujID7n5PVKVCpA7EQs7?gv=true" style="border: 0" width="100%" height="600" frameborder="0"')

if __name__ == '__main__':
    app.run(debug=True)