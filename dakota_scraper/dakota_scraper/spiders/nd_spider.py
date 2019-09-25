import scrapy
import scrapy_splash

import matplotlib

class DakotaSpider(scrapy.Spider):
    name = 'nd'

    def start_requests(self):
        url = "https://firststop.sos.nd.gov/api/Records/businesssearch"
        yield scrapy.FormRequest(url=url, callback=self.parse, method='POST', headers={
            #POST / api / Records / businesssearch
        #HTTP / 1.1
        'Accept': '*/*',
        'Accept-Language': 'en-US, en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'firststop.sos.nd.gov',
        #'Connection': 'keep-alive',
        #'content-length': '67',
            'authorization': 'undefined',
            'Content-Type': 'application/json',
            'origin': 'https://firststop.sos.nd.gov',
            'referer': 'https://firststop.sos.nd.gov/search/business',
            'Sec-Fetch-Mode': 'cors',
            'User-Agent': 'Mozilla/5.0'
        }, formdata={'"SEARCH_VALUE"': '"X"', '"STARTS_WITH_YN"': '"true"', '"ACTIVE_ONLY_YN"': 'false'})

    def parse(self, response):
        print(response.body)
        #js = response.urljoin(script.attrib['src'])
        # script = """
        #         function main(splash)
        #             assert(splash:go(splash.args.url))
        #             return splash:evaljs("document.title")
        #         end
        #         """
        # #yield scrapy.Request(js, callback=self.splash_parse) #, args={'lua_source':script})
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
