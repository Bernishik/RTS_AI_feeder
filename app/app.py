import crochet
from scrapy.utils.project import get_project_settings

crochet.setup()

from flask import Flask, jsonify
from scrapy.crawler import CrawlerRunner
from crawler.spiders.quote_scraper import QuoteSpider
from crawler.spiders.biorxiv_covid_scraper import BiorxivCovidScraper

app = Flask(__name__)
crawl_runner = CrawlerRunner(get_project_settings())
quotes_list = []
scrape_in_progress = False
scrape_complete = False


@app.route('/')
def crawl_for_quotes():

    global scrape_in_progress
    global scrape_complete
    global scrape_complete

    if not scrape_in_progress:
        scrape_in_progress = True
        global quotes_list

        scrape_with_crochet(quotes_list)
        return 'SCRAPING'

    if scrape_complete:
        print()
        return "ok"

    return 'SCRAPE IN PROGRESS'


@crochet.run_in_reactor
def scrape_with_crochet(_list):
    # eventual = crawl_runner.crawl(QuoteSpider, quotes_list=_list)
    eventual = crawl_runner.crawl(BiorxivCovidScraper, quotes_list=_list)
    eventual.addCallback(finished_scrape)


def finished_scrape(null):
    global scrape_complete
    scrape_complete = True


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8001,debug=True)
