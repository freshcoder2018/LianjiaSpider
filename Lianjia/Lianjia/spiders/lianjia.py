# -*- coding: utf-8 -*-
import scrapy
from Lianjia.items import LianjiaItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['https://gz.lianjia.com/chengjiao/']
    start_urls = ['https://gz.lianjia.com/chengjiao/']

    def parse(self, response):
        qu_list = response.xpath('//div[@class="position"]/dl/dd/div/div//a/@href').extract()
        for qu in qu_list:
            qu_url = self.start_urls[0] + qu.split('/')[2]
            yield scrapy.Request(url=qu_url, callback=self.parse_qu, dont_filter=True)

    def parse_qu(self, response):
        min_list = response.xpath('//div[@class="position"]/dl/dd/div/div[2]//a/@href').extract()
        for min in min_list:
            if min not in response.url:
                min_url = self.start_urls[0] + min.split('/')[2]
                yield scrapy.Request(url=min_url, callback=self.parse_min, dont_filter=True)

    def parse_min(self, response):
        house_urls = response.xpath('//div[@class="content"]//ul[@class="listContent"]//div[@class="title"]/a/@href').extract()
        for house_url in house_urls:
            yield scrapy.Request(url=house_url, callback=self.parse_house, dont_filter=True)

    def parse_house(self, response):
        next_urls = response.xpath('//div[contains(@class, house-lst-page-box)]//a[position>1]/@href').extract()
        if next_urls:
            for next_url in next_urls:
                next_url = response.urljoin(next_url)
                yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)
        item = LianjiaItem()
        item['avgPrice'] = response.xpath('//div[@class="price"]/span/i/text()').extract_first() + '万'
        item['dealTotalPrice'] = response.xpath('//div[@class="price"]/b/text()').extract_first() + '元/平'
        yield item