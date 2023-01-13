import scrapy

class JobSpider(scrapy.Spider):
    name = "job_spider"
    start_urls = []

    def start_requests(self, jobtitle=None, location=None):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={'jobtitle': jobtitle, 'location': location})

    def parse(self, response):
        jobtitle = response.meta.get('jobtitle')
        location = response.meta.get('location')
        
        # Use CSS or XPath selectors to extract job listings
        job_listings = response.css('div.job-listing')
        for job in job_listings:
            yield {
                'title': job.css('h2 a::text').get(),
                'location': job.css('div.job-location::text').get(),
                'description': job.css('div.job-description::text').get()
            }