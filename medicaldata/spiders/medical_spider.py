#!/usr/bin/python
# -*- coding:utf-8 -*-
# **************************
# * Author      :  baiyyang
# * Email       :  baiyyang@163.com
# * Description :  
# * create time :  2017/11/15下午7:23
# * file name   :  medical_spider.py

import scrapy
from ..items import MedicaldataItem
import urllib2
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MedicalSpider(scrapy.Spider):
    name = 'medical'
    allowed_domain = ['jibing.wenyw.com']  # 约定搜索域
    start_urls = ['http://jibing.wenyw.com']

    def parse(self, response):
        """获取按拼音首字母的路径"""
        links = response.xpath('//div[@class="submenu02"]/a/@href').extract()
        for link in links:
            # url = response.urljoin(link)
            yield scrapy.Request(link, callback=self.parser_pinyin)

    def parser_pinyin(self, response):
        """获取每个疾病名称的路径"""
        diseases = response.xpath('//ul[@class="block08 block08c"]/li/a/@href').extract()
        for disease in diseases:
            # 将相对url拼接成绝对url
            # url = response.urljoin(disease)
            yield scrapy.Request(disease, callback=self.parser_disease)

        # 递归爬取下一页数据
        nextPage = response.xpath('//div[@class="pageStyle"]/p/a/@href').extract()
        nextText = response.xpath('//div[@class="pageStyle"]/p/a/text()').extract()
        for i, text in enumerate(nextText):
            if text.strip() == '下一页':
                SITE_URL = 'http://jibing.wenyw.com'
                nextURL = SITE_URL + nextPage[i]
                yield scrapy.Request(nextURL, callback=self.parser_pinyin)

    def parser_disease(self, response):
        """根据疾病name下载疾病信息"""
        item = MedicaldataItem()
        item['title'] = response.xpath('//ul[@class="submenu01b"]/div/h2/a/text()').extract()[0]
        details = response.xpath('//ul[@class="submenu01c"]/li/a/@href').extract()
        SITE_URL = 'http://jibing.wenyw.com'
        url = SITE_URL + details[0]
        yield scrapy.Request(url, meta={'item': item, 'index': 0, 'details': details},
                             callback=self.parser_detail)
        # # 下载疾病的对应的信息，概述，病因，症状，化验结果，治疗方法，并发症，
        # # 如何预防，饮食保健
        # names = ['description', 'reason', 'symptom', 'examination',
        #          'treatment', 'complication', 'prevention', 'care']
        # for i, detail in enumerate(details):
        #     # 将相对路径拼接成绝对url
        #     url = response.urljoin(detail)
        #     req = urllib2.Request(url)
        #     req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64)"
        #                                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")
        #     try:
        #         res = urllib2.urlopen(req)
        #         content = res.read()
        #         root = etree.HTML(content)
        #         cont = root.xpath('//div[@class="detailc"]//p/text()')
        #         item[names[i]] = ''.join(cont)
        #     except urllib2.HTTPError as e:
        #         print e.reason
        #     # content_response = scrapy.http.Response(str(url))
        #     # content = content_response.xpath('//div[@class="detailc"]//p/text()').extract()
        #     # item[names[i]] = ''.join(content)
        # return item

    def parser_detail(self, response):
        # 下载疾病的对应的信息，概述，病因，症状，化验结果，治疗方法，并发症，
        # 如何预防，饮食保健
        names = ['description', 'reason', 'symptom', 'examination',
                 'treatment', 'complication', 'prevention', 'care']
        item = response.meta['item']
        index = response.meta['index']
        details = response.meta['details']
        content = response.xpath('//div[@class="detailc"]/p/text()').extract()
        item[names[index]] = ''.join(content)
        SITE_URL = 'http://jibing.wenyw.com'
        index += 1
        if index > 7:
            yield item
        else:
            url = SITE_URL + details[index]
            yield scrapy.Request(url, meta={'item': item, 'index': index, 'details': details},
                                 callback=self.parser_detail)





