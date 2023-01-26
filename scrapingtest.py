import bs4
import requests
import json
from urllib.parse import urljoin

jobtitle = 'python'
location = 'remote'

url = f'https://www.flexjobs.com/search?search={jobtitle}&location={location}&srt=date'
pages = []
paginationItems = []

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

pagination('python','remote')
for i in paginationItems:
    print(i['href'])