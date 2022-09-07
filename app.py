from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    # the path to this might need to be modified when deployed
    return send_file('static/pdf/resume.pdf')

@app.route('/poster')
def poster():
    return send_file('static/pdf/Meyer_2022_symposium_poster_Final.pdf')
