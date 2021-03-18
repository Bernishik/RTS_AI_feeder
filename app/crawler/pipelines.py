import json

from .items import QuoteItems
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerPipeline:
    def process_item(self, item, spider):
        return item
# class QuotePipeline:
#     def open_spider(self, spider):
#         self.file = open('items.jl', 'w')
#
#     def close_spider(self, spider):
#         self.file.close()
#     def process_item(self,item,spider):
#         line = json.dumps(ItemAdapter(item).asdict()) + "\n"
#         self.file.write(line)
#         return item

# class BiorxivCovidSacraperPipeline:
#     def open_spider(self, spider):
#         # self.file = open('items.json', 'w')
#         pass
#
#     def close_spider(self, spider):
#         pass
#         # self.file.close()
#     def process_item(self,item,spider):
#         # line = json.dumps(ItemAdapter(item).asdict()) + "\n"
#         # self.file.write(line)
#         print(item["title"])
#         return item
