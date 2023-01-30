from flask import Flask, render_template, request
import bs4
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # scrape()
    return render_template('index.html')

def flexjobs_scraper(url):
    res = requests.get(url)
    res.raise_for_status()
    job_listings = []

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # nextLink = soup.select('a[rel="next"]')[0].get('href')

    # Gett all the jos on the search
    jobs = soup.select('.row .job')
    print(len(jobs))
    for job in jobs:
        j = {
            'title': job.select('.job-title')[0].get_text(),
            'href': 'https://www.flexjobs.com' + job.select('.job-title')[0].attrs['href'],
            'location': job.select('.job-locations')[0].get_text(),
            'description': job.select('.job-description')[0].get_text()
        }  
        # print(j)
        job_listings.append(j)
    
    # save the result into Json File
    # with open('data.json', 'w') as f:
    #     json.dump(job_listings, f)
        # next button
        # nextLink = soup.select('a[rel="next"]')[0].get('href')
        # url = 'https://flexjobs.com' + nextLink
        # flexjobs_scraper(url)
    
    # scrap the pagination link
    # pagesnav = soup.select('.page-link')
    # # get the the first and the last page on the scraped website
    # lastnumber = int(pagesnav[len(pagesnav) - 2].get_text())
    # firstnumber = int(pagesnav[len(pagesnav) + 1 - len(pagesnav)].get_text())
    # # generating a list of pagination items, page number and page link
    # for i in range(firstnumber, lastnumber + 1):
    #     full_url = url + f'&page={i}'
    #     paginationItems.append({
    #         'pageNumber':int(i),
    #         'href': full_url
    #     })

    return job_listings


@app.route('/pagination', methods=['POST'])
def changepage():
    # getting the selected page and link
    currentPage = int(request.form['currentPage'])
    href = str(request.form['href'])
    
    list = flexjobs_scraper(href)[0]
    paginationItems = flexjobs_scraper(href)[1]

    # return render_template('index.html')
    return render_template('jobs.html', job_listings=list, paginationItems=paginationItems, currentPage=currentPage)
    # Do something with the page number, like querying a database for data for that page
    

@app.route('/scrape', methods=['POST'])
def scrape():
    jobtitle = request.form['jobtitle']
    location = request.form['location']
    
    url = f'https://www.flexjobs.com/search?search={jobtitle}&location={location}&srt=date&page=1'
    try:
        job_listings = flexjobs_scraper(url)
    except:
        print(len(job_listings))

    return render_template('jobs.html', job_listings=job_listings, results=len(job_listings))