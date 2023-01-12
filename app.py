from flask import Flask, render_template
import json, requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    # jobtitle = request.form['jobtitle']
    # location = request.form['location']
    # Do something with the form data
    return 'Scraping...'
