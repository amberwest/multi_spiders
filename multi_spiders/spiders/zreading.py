# -*- coding: utf-8 -*-
import scrapy
from multi_spiders.items import MultiSpidersItem, NewLoader


class ZreadingSpider(scrapy.Spider):
    name = 'zreading'
    allowed_domains = ['zreading.cn']
    start_urls = ['http://www.zreading.cn/']

    def parse(self, response):
        articles = response.css('.blockGroup article')
        for article in articles:
            item = NewLoader(item=MultiSpidersItem(), response=response)
            title = article.css('header h2 a::text').extract()
            item.add_value('title', title)

            url = article.css('header h2 a::attr(href)').extract()
            item.add_value('url', url)

            info = article.css('footer ::text').extract()
            item.add_value('info', info)

            item.add_value('source', '左岸读书')

            yield item.load_item()
