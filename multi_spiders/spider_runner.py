#! -*- coding:utf-8 -*-
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from multi_spiders.spiders.zreading import ZreadingSpider
from multi_spiders.spiders.yueguang import YueguangSpider

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

runner = CrawlerRunner()
runner.crawl(ZreadingSpider)
runner.crawl(YueguangSpider)

d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()

