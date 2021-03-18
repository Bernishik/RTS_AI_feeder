import re
from time import sleep

import scrapy
import json
import os
# parse site
from crawler.items import BiorxivCovidItem


class BiorxivCovidScraper(scrapy.Spider):
    start_urls = ['https://connect.biorxiv.org/relate/content/181?page=1']
    visited_urls = []
    name = 'BiorxivCovid'
    counter_page = 0
    counter_subpage = 0

    def cleanhtml(self, text):
        TAG_RE = re.compile(r'<[^>]+>')
        return TAG_RE.sub('', text)

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)
            sites = response.xpath("//span[@class='highwire-cite-title']//@href").extract()
            self.counter_page += 1
            for site in sites:
                self.counter_subpage += 1
                yield response.follow(site, callback=self.parse_data, meta={"site": response, "page": self.counter_page,
                                                                            "subpage": self.counter_subpage})
            self.counter_subpage = 0

            next_page = response.xpath('//li[@class="pager-next first last"]//@href').extract_first()

            if next_page is not None:
                yield response.follow(next_page)

    def parse_data(self, response):
        site = response.meta['site'].url.split('/')[2]
        page = response.meta['page']
        subpage = response.meta['subpage']
        item = BiorxivCovidItem()
        item["source"] = response.url
        item["title"] = response.xpath("//h1[@id='page-title']/text()").extract_first()
        item["data"] = " ".join(response.xpath(
            "//div[@class='panel-pane pane-custom pane-1']/div[@class='pane-content']/text()").extract_first().split())
        item["text"] = response.xpath("//p[@id='p-2']/text()").extract_first()
        item["competing_interest_statement"] = response.xpath("//p[@id='p-3']/text()").extract_first()
        item["funding_statement"] = response.xpath("//p[@id='p-4']/text()").extract_first()
        # missing author_declarations TODO
        authors_names = \
            response.xpath("//div[@class='highwire-cite-authors']/span[@class='highwire-citation-authors']")[0].xpath(
                "span['highwire-citation-author']/span[@class='nlm-given-names']/text()").extract()
        authors_surnames = \
            response.xpath("//div[@class='highwire-cite-authors']/span[@class='highwire-citation-authors']")[0].xpath(
                "span['highwire-citation-author']/span[@class='nlm-surname']/text()").extract()
        authors = []
        for name, surname in zip(authors_names, authors_surnames):
            authors.append(name + ' ' + surname)
        item["authors"] = authors

        filename = "./extracted_data/" + str(site) + "/" + str(page) + "/posts-%s.json" % str(subpage)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write(json.dumps(dict(item), indent=4))
        yield item
        return
