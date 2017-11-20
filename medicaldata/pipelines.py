# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


class MedicaldataPipeline(object):
    def __init__(self):
        #
        self.titles_set = set()

        # 链接数据库
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        db_name = settings['MONGO_DB']
        coll = settings['MONGO_COLL']
        self.client = pymongo.MongoClient(host=host, port=port)
        # 获得数据库的句柄
        self.db = self.client[db_name]
        # 获得collection的句柄
        self.coll = self.db[coll]

    def process_item(self, item, spider):
        postItem = dict(item)
        if postItem['title'] not in self.titles_set:
            self.titles_set.add(postItem['title'])
            self.coll.insert(postItem)
        else:
            pass
        return item
