# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Conference=scrapy.Field()
    City=scrapy.Field()
    Deadline=scrapy.Field()
    Date=scrapy.Field()
    Notification=scrapy.Field()
    FormatAndComemnt=scrapy.Field()
    Remark=scrapy.Field()
    FinalVersion=scrapy.Field()
    EarlyRegistration=scrapy.Field()
    Year=scrapy.Field()
    StartingDate=scrapy.Field()
    EndingDate=scrapy.Field()
    FullNameConference=scrapy.Field()