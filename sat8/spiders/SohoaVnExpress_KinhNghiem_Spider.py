# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


from AbstractPostSpider import AbstractPostSpider

class SohoaVnExpress_KinhNghiem_Spider(AbstractPostSpider):
    name = "blog_spider"
    allowed_domains = ["sohoa.vnexpress.net", ]

    config_urls = [
        {
            "url" : "http://sohoa.vnexpress.net/tin-tuc/kinh-nghiem/page/[0-9]+.html",
            "max_page" : 15
        }
    ]

    configs = {
        "links" : '//*[@class="title_news"]//a[1]/@href',
        'title' : '//*[@class="title_news"]/h1//text()',
        'teaser' : '//*[@class="short_intro txt_666"]//text()',
        'avatar' : '//*[@id="article_content" or contains(@class,"fck_detail width_common")]//img[1 or 2 or 3 or 4]/@src',
        'content' : '//*[@id="article_content" or contains(@class,"fck_detail width_common")]',
        'category_value' : 'Kinh nghiệm',
        'type' : 'post',
        'category_id' : 4
    }
