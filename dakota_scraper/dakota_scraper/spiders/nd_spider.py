import scrapy
import scrapy_splash

import matplotlib

class DakotaSpider(scrapy.Spider):
    name = 'nd'

    def start_requests(self):
        url = "https://firststop.sos.nd.gov/search/business"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        script = response.css('script')[0]
        js = response.urljoin(script.attrib['src'])
        script = """
                function main(splash)
                    assert(splash:go(splash.args.url))
                    return splash:evaljs("document.title")
                end
                """
        yield scrapy.Request(js, callback=self.splash_parse) #, args={'lua_source':script})
        #print(js)

    def splash_parse(self, response):
        print(response.body_as_unicode())

from scrapy.crawler import CrawlerProcess

class MySpider(DakotaSpider):
    # Your spider definition
    ...

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json'
})

process.crawl(MySpider)
process.start()
