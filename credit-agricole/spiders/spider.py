import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import CreditagricoleItem
from itemloaders.processors import TakeFirst


class CreditagricoleSpider(scrapy.Spider):
	name = 'credit-agricole'
	start_urls = ['https://www.credit-agricole.it/crpr/news-ed-eventi']

	def parse(self, response):
		post_links = response.xpath('//a[@class="news-box__more link-chevron"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//span[@class="next"]/a/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="description"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//h2[@class="rf-text rf-text__subtitle"]/text()').get()

		item = ItemLoader(item=CreditagricoleItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
