from flask import Flask, render_template, request
from scrapy.utils.project import get_project_settings
from scraper.spider import JobSpider
from scrapy.crawler import CrawlerProcess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/scraper', methods=['POST'])
def scrape():
    jobtitle = request.form['jobtitle']
    location = request.form['location']
    # Do something with the form data
    # print(jobtitle, location)
    process = CrawlerProcess(get_project_settings())
    process.crawl(JobSpider, jobtitle=jobtitle, location=location)
    process.start()

    return f'<h1>{jobtitle} {location}<h1>'