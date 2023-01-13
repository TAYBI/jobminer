import scrapy


class JobSpider(scrapy.Spider):
    name = "job_spider"

    def __init__(self, jobtitle=None, location=None, *args, **kwargs):
        super(JobSpider, self).__init__(*args, **kwargs)
        self.jobtitle = jobtitle
        self.location = location
        self.start_urls = [f'https://www.flexjobs.com/search?search={jobtitle}&location={location}']

    def parse(self, response):
        # Use CSS selectors to extract job listings
        job_listings = response.css('.row .job')
        for job in job_listings:
            yield {
                'title': job.css('.job-title::text').get(),
                'location': job.css('div.job-locations::text').get(),
                'description': job.css('div.job-description').get()
            }

        
        # next_url = 'https://www.flexjobs.com' + \
        #     response.css('a[rel="next"]').attrib['href']

        # if next_url is not None:
        #     yield response.follow(next_url, callback=self.parse)