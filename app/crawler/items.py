# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuoteItems(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class BiorxivCovidItem(scrapy.Item):
    source = scrapy.Field()
    title = scrapy.Field()
    authors = scrapy.Field()
    text = scrapy.Field()
    competing_interest_statement = scrapy.Field()
    funding_statement = scrapy.Field()
    author_declarations = scrapy.Field()
    data = scrapy.Field()
