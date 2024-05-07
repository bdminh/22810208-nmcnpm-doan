# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CrawlerAheadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type=scrapy.Field()
    conference=scrapy.Field()
    city=scrapy.Field()
    deadline=scrapy.Field()
    date=scrapy.Field()
    notification=scrapy.Field()
    format_and_comemnt=scrapy.Field()

class CrawlerCCFItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type=scrapy.Field()
    conference=scrapy.Field()
    description=scrapy.Field()
    place=scrapy.Field()
    year=scrapy.Field()
    date=scrapy.Field()
    deadline=scrapy.Field()
    timezone=scrapy.Field()
    website=scrapy.Field()
    note=scrapy.Field()


class CrawlerRunningItem(scrapy.Item):
    type=scrapy.Field()
    conference=scrapy.Field()
    city=scrapy.Field()
    date=scrapy.Field()
    remark=scrapy.Field()

class CrawlerFutureItem(scrapy.Item):
    type=scrapy.Field()
    conference=scrapy.Field()
    city=scrapy.Field()
    date=scrapy.Field()
    notification=scrapy.Field()
    final_version=scrapy.Field()
    early_registration=scrapy.Field()
    remark=scrapy.Field()

class CrawlerPlanningItem(scrapy.Item):
    type=scrapy.Field()
    conference=scrapy.Field()
    year=scrapy.Field()
    city=scrapy.Field()
    starting_date=scrapy.Field()
    ending_date=scrapy.Field()
    remark=scrapy.Field()
    
class CrawlerFullnameItem(scrapy.Item):
    type=scrapy.Field()
    conference=scrapy.Field()
    conference_fullname=scrapy.Field()










