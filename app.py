from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume.pdf')
def resume():
    # the path to this might need to be modified when deployed
    return send_file('static/pdf/resume.pdf')

@app.route('/poster.pdf')
def poster():
    return send_file('static/pdf/Meyer_2022_symposium_poster_Final.pdf')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)