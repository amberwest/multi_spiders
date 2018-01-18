# -*- coding: utf-8 -*-
import scrapy
from multi_spiders.items import MultiSpidersItem, NewLoader


class YueguangSpider(scrapy.Spider):
    name = 'yueguang'
    allowed_domains = ['williamlong.info']
    start_urls = ['http://williamlong.info/']

    def parse(self, response):
        articles = response.xpath('//*[@id="divMain"]/div[contains(@class, "cate5")]')
        for article in articles:
            item = NewLoader(item=MultiSpidersItem(), response=response)

            title = article.css('h2 a::text').extract()
            item.add_value('title', title)

            url = article.css('h2 a::attr(href)').extract()
            item.add_value('url', url)

            info = ''.join(article.css('h6 ::text').extract()[:-2]).split(' | ')
            item.add_value('info', info)

            item.add_value('source', '月光博客')

            yield item.load_item()
