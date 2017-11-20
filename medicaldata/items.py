# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MedicaldataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 疾病名称
    description = scrapy.Field()  # 概述
    reason = scrapy.Field()  # 病因
    symptom = scrapy.Field()  # 症状
    examination = scrapy.Field()  # 检查
    treatment = scrapy.Field()  # 治疗方案
    complication = scrapy.Field()  # 并发症
    prevention = scrapy.Field()  # 预防
    care = scrapy.Field()  # 饮食保健

