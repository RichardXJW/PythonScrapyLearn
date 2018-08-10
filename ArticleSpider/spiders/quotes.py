# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            yield {
            'text': quote.css('.text::text').extract_first(),
            'author': quote.css('.author::text').extract_first(),
            'tags': quote.css('.tags .tag::text').extract()
            }
        next_page = response.css('.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#
#     def start_requests(self):
#         urls = ['http://quotes.toscrape.com']
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         page = response.url
#         print('='*120)
#         print(response.body)
#         print('='*120)
#         pass