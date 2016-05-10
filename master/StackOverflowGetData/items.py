# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowqaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question=scrapy.Field()
    answers=scrapy.Field()
    link=scrapy.Field()
    up_count=scrapy.Field()
    down_count=scrapy.Field()
    favorite=scrapy.Field()
    num_answers=scrapy.Field()
    asked=scrapy.Field()
    user=scrapy.Field()
    reputation=scrapy.Field()
    views=scrapy.Field()
    active=scrapy.Field()
    pass
