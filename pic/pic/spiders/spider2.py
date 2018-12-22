# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.http import HtmlResponse
from ..items import PicItem

class SpiderSpider(scrapy.Spider):
    name = 'spider_2'
    start_urls = ['http://777sds.com/html/artlist/262_{}.json'.format(i) for i in range(1,54)]

    def parse(self, response):
        url_list=['http://7777sds.com/html/artdata/{}.json'.format(i['s_id']) for i in json.loads(response.text)['list']]
        for i in url_list:
            yield scrapy.Request(url=i, callback=self.parse_pic)

    def parse_pic(self,response):
        item = PicItem()
        info=json.loads(response.text)
        item['title']=info['s_name']
        item['image_urls'] = HtmlResponse(url=response.url,body=info['s_body'].encode('utf8')).xpath('//img/@src').extract()
        item['name']=[str(i) for i in range(0,len(item['image_urls']))]
        yield item


                
