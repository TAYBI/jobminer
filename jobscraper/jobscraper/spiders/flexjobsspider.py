import scrapy
from scrapy.crawler import CrawlerProcess

class JobSpider(scrapy.Spider):
    name = "flexjobs_spider"

    def __init__(self, jobtitle=None, location=None, *args, **kwargs):
        super(JobSpider, self).__init__(*args, **kwargs)
        self.jobtitle = 'hdjd'
        self.location = location
        self.start_urls = [f'https://www.flexjobs.com/search?search={jobtitle}&location={location}']

    def parse(self, response):
        
        # Use CSS selectors to extract job listings
        job_listings = response.css('.row .job')
        print(job_listings)
        for job in job_listings:
            yield {
                    'title': job.css('.job-title::text').get(),
                    'location': job.css('div.job-locations::text').get(),
                    'description': job.css('div.job-description').get()
            }

        next_url = 'https://www.flexjobs.com' + \
            response.css('a[rel="next"]').attrib['href']

        if next_url is not None:
            # yield scrapy.Request(url= next_url)
            yield response.follow(next_url, callback=self.parse)

# c = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/5.0',
#     'FEED_FORMAT': 'json',
#     'FEED_URI': 'data.json',
# })
# c.crawl(JobSpider)
# c.start()