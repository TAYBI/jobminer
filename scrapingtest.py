import bs4
import requests
import json

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

    for element in pagesnav:
        text = element.select('.page-link')[0].get_text()
        print(text)
    # Do something with the text and link

   


# try:
flexjobs_scraper(url)
# except:
#     print(len(pages))
