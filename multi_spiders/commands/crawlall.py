# _*_ coding:utf-8 _*_

from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    # 源码https://github.com/scrapy/scrapy/blob/master/scrapy/commands/crawl.py
    def run(self, args, opts):
        spider_loader = self.crawler_process.spider_loader
        for spidername in args or spider_loader.list():
            self.crawler_process.crawl(spidername)
        self.crawler_process.start()