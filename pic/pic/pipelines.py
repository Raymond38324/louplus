# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
class PicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for i in item['image_urls']:
            yield Request(i, meta={'name': item['name'][item['image_urls'].index(i)],"folder":item['title']})

    def file_path(self, request, response=None, info=None):
        return '{}/{}.jpg'.format(request.meta['folder'],request.meta['name'])

