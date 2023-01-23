from flask import Flask, render_template, request
from jobscraper.jobscraper.spiders.flexjobsspider import JobSpider
import bs4
import requests

app = Flask(__name__)
job_listings = []
paginationItems = []

@app.route("/")
def index():
    return render_template('index.html')

def flexjobs_scraper(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    nextLink = soup.select('a[rel="next"]')[0].get('href')

    jobs = soup.select('.row .job')

    print(len(jobs))
    for job in jobs:
        j = {
            'title': job.select('.job-title')[0].get_text(),
            'location': job.select('.job-locations')[0].get_text(),
            'description': job.select('.job-description')[0].get_text()
        }
        print(j)
        job_listings.append(j)
        # next button
        # nextLink = soup.select('a[rel="next"]')[0].get('href')
        # url = 'https://flexjobs.com' + nextLink
        # flexjobs_scraper(url)

def pagination(jobtitle, location):
    res = requests.get(f'https://www.flexjobs.com/search?search={jobtitle}&location={location}&srt=date')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    pagesnav = soup.select('.page-link')

    lastnumber = int(pagesnav[len(pagesnav) - 2].get_text())
    firstnumber = int(pagesnav[len(pagesnav) + 1 - len(pagesnav)].get_text())

    for i in range(firstnumber, lastnumber + 1):
        full_url = f'https://www.flexjobs.com/search?search={jobtitle}&location={location}&srt=date&page={i}'
        paginationItems.append({
            'pageNumber': i,
            'href': full_url
        })

@app.route('/scrape', methods=['POST'])
def scrape():
    jobtitle = request.form['jobtitle']
    location = request.form['location']

    url = f'https://www.flexjobs.com/search?search={jobtitle}&location={location}&srt=date'
    try:
        flexjobs_scraper(url)
    except:
        print(len(job_listings))

    
    return render_template('jobs.html', job_listings=job_listings)
    