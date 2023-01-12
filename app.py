from flask import Flask, render_template, request
import json, requests
import scrapy
from scrapy.crawler import CrawlerProcess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    jobtitle = request.form['jobtitle']
    location = request.form['location']
    # Do something with the form data
    # print(jobtitle, location)
    
    return f'<h1>{jobtitle} {location}<h1>'
