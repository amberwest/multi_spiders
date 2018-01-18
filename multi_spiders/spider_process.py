#! -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerProcess

from multi_spiders.spiders.zreading import ZreadingSpider
from multi_spiders.spiders.yueguang import YueguangSpider
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(settings=get_project_settings())
# 同个进程
process.crawl(ZreadingSpider)
process.crawl(YueguangSpider)

process.start()