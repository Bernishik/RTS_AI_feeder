import re

import scrapy
import json
import os
# parse site
from crawler.items import QuoteItems


class QuoteSpider(scrapy.Spider):
    start_urls = ['http://quotes.toscrape.com/page/1/']
    name = 'quote'
    quotation_mark_pattern = re.compile(r'[“|”]')
    # custom_settings = {'FEED_URI': "data/aliexpress_%(time)s.json",
    #                    'FEED_FORMAT': 'json',
    #                    'FEED_EXPORT_ENCODING' : 'utf-8'}
    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)


    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        page = response.url.split('/')[-2]
        page_quote =[]
        for quote in quotes:
            item = QuoteItems()
            item["quote"] =self.quotation_mark_pattern.sub('',quote.xpath('.//span[@class="text"]/text()').extract_first())
            item["author"] = quote.xpath('.//span//small[@class="author"]/text()').extract_first()


            item["tags"] = []
            for tag in quote.xpath('.//div[@class="tags"]//a[@class="tag"]/text()'):
                item["tags"].append(tag.extract())
            self.quotes_list.append({
                'quote': item["quote"],
                'author': item["author"],
                'tags': item["tags"]})
            page_quote.append({
                'quote': item["quote"],
                'author': item["author"],
                'tags': item["tags"]})
            yield item

        # writing data in files
        filename = "./extracted_data/quotes.toscrape.com/%s/posts.json" % page
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write(json.dumps(page_quote,indent=4))


        next_page = response.xpath('//nav//ul//li[@class="next"]//@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page)
