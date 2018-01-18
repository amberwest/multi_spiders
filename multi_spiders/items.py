# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, TakeFirst, Identity


class NewLoader(ItemLoader):
    """重写item loader，默认取第一个"""
    default_output_processor = TakeFirst()

class MultiSpidersItem(scrapy.Item):
    title = scrapy.Field()
    # info仍然返回列表
    info = scrapy.Field(
        input_processor=Compose(lambda x: (d.strip() for d in x if d.strip() and d.strip() not in ['•', '|', 'by'])),
        output_processor=Identity()
    )
    url = scrapy.Field()
    source = scrapy.Field()
