# -*- coding: utf-8 -*-
import scrapy


class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['foxmovies.com']
    start_urls = ['https://www.foxmovies.com/movies/deadpool-2/']

    def parse(self, response):
        yield {
            'title': response.css('div.header-titles h1::text').extract_first(),
            'availability': response.css('div.header-titles h2::text').extract_first(),
            'synopsis': response.css('div.synopsis p::text').extract_first(),
            'genre': response.css('div.genres p::text').extract_first(),
            'runtime': response.css('div.runtime p::text').extract_first(),
            'director': response.css('div.crew  p::text').extract_first(),
        }
        

