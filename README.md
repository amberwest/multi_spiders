### 运行多个spider文件的三种方法
1. spider_process.py
    * 终端运行 `python3 -m multi_spiders.spider_process`
    
2. spider_runner.py(同上)

3. commands
    * 该文件夹与spiders文件夹同级目录
    * commands是个package,即要有__init__.py
    * 运行文件 `crawlall.py`
    * settings.py文件要添加一行代码，`COMMANDS_MODULE = ‘multi_spiders.commands'`
    * 终端运行 `scrapy crawlall`