import bs4
import requests
import json
from urllib.parse import urljoin

jobtitle = 'python'
location = 'remote'

url = f'https://www.flexjobs.com/search?search={jobtitle}&location={location}&srt=date'
pages = []


def flexjobs_scraper(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # nextLink = soup.select('a[rel="next"]')[0].get('href')

    # while nextLink:
    pagesnav = soup.select('.page-link')
    # firstnumber = int(pagesnav[len(pagesnav) + 1 - len(pagesnav)].get_text())
    # print(pagesnav)
    for element in pagesnav:
        relative_url = element.get('href')
        full_url = urljoin('https://www.flexjobs.com', relative_url)
        print(full_url)
    # Do something with the text and link

   


# try:
flexjobs_scraper(url)
# except:
#     print(len(pages))
