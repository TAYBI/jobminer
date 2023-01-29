from flask import Flask, render_template, request
import bs4
import requests
import json

app = Flask(__name__)
job_listings = []
paginationItems = []
currentPage = 1

@app.route("/")
def index():
    # scrape()
    return render_template('index.html')
    # render_template('jobs.html', job_listings=job_listings, paginationItems=paginationItems, currentPage=currentPage)

def flexjobs_scraper(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # nextLink = soup.select('a[rel="next"]')[0].get('href')

    # Gett all the jos on the search
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
    
    # save the result into Json
    with open('data.json', 'w') as f:
        json.dump(job_listings, f)
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
            'pageNumber':int(i),
            'href': full_url
        })


@app.route('/pagination', methods=['POST'])
def changepage():
    currentPage = request.form['currentPage']
    href = request.form['href']

    print('*' * 30)
    print(currentPage, href)
    print('*' * 30)
    flexjobs_scraper(href)
    return render_template('jobs.html', job_listings=job_listings, paginationItems=paginationItems, currentPage=currentPage)
    # Do something with the page number, like querying a database for data for that page
    

@app.route('/scrape', methods=['POST'])
def scrape():
    # jobtitle = request.form['jobtitle']
    # jobtitle = request.form['jobtitle']
    jobtitle = 'python'
    location = 'remote'

    url = f'https://www.flexjobs.com/search?search={jobtitle}&location={location}&srt=date'
    try:
        flexjobs_scraper(url)
        pagination(jobtitle, location)
    except:
        print(len(job_listings))

    return render_template('jobs.html', job_listings=job_listings, paginationItems=paginationItems, currentPage=currentPage)
    
    