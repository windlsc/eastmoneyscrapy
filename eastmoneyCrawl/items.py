# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class fundDetailItem(scrapy.Item):
    fund_name = scrapy.Field()
    fund_abbreviated_name = scrapy.Field()
    fund_id = scrapy.Field()
    fund_type = scrapy.Field()
    fund_issue_date scrapy.Field()
    fund_start_date scrapy.Field()
    fund_scale = scrapy.Field()
    fund_welfare = scrapy.Field()
    fund_manager = scrapy.Field()
    fund_trustee = scrapy.Field()
    fund_handler = scrapy.Field()
    fund_bonus = scrapy.Field()
    fund_fee = scrapy.Field()
    fund_trustee_fee = scrapy.Field()
    fund_service_fee = scrapy.Field()
    fund_max_warrant_fee = scrapy.Field()
    fund_purchase_fee  = scrapy.Field()
    fund_redemptin_fee = scrapy.Field()
    fund_base_line = scrapy.Field()
    fund_trace = scrapy.Field()


