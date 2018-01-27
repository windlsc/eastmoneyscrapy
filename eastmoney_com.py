# -*- coding: utf-8 -*-
import re

from selenium import webdriver

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EastmoneyComSpider(CrawlSpider):
    name = 'eastmoney_com'
    allowed_domains = ['http://fund.eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/fundguzhi.html']

    #rules = (
    #    Rule(LinkExtractor(allow=r'f10/\d+\.html'), callback='parse_fund', follow=True),
    #)
    def parse(self, response):
        urls = response.xpath("//div[@id='otableWrap']//tbody/tr//a/@href")
        for url in urls:
            if re.match('f\d+/\d+\.html', url):
                full_url = response.url + url
                click_response
                request = scrapy.Request(url=full_url, callback=self.parse_fund)

    def parse_fund(self, response):
        fund_name = response.xpath("//div[@class='txt_cont']/descendant::table/tr[1]/td[1]/text()").extract_first() 
        fund_abbreviated_name = response.xpath("//div[@class='txt_cont']/descendant::table/tr[1]/td[2]/text()").extract_first()
        fund_id = response.xpath("//div[@class='txt_cont']/descendant::table/tr[2]/td[1]/text()").extract_first()
        fund_type = response.xpath("//div[@class='txt_cont']/descendant::table/tr[2]/td[2]/text()").extract_first()
        fund_issue_date = response.xpath("//div[@class='txt_cont']/descendant::table/tr[3]/td[1]/text()").extract_first()
        fund_start_date = response.xpath("//div[@class='txt_cont']/descendant::table/tr[3]/td[2]/text()").extract_first()
        fund_scale = response.xpath("//div[@class='txt_cont']/descendant::table/tr[4]/td[1]/text()").extract_first()
        fund_welfare = response.xpath("response.xpath("//div[@class='txt_cont']/descendant::table/tr[4]/td[2]/a/text()).extract_first()
        fund_manager = response.xpath("//div[@class='txt_cont']/descendant::table/tr[5]/td[1]/a/text()").extract_first()
        fund_trustee = response.xpath("//div[@class='txt_cont']/descendant::table/tr[5]/td[2]/a/text()").extract_first()
        fund_handler = response.xpath("//div[@class='txt_cont']/descendant::table/tr[6]/td[1]/a/text()").extract_first() 
        fund_bonus = response.xpath("//div[@class='txt_cont']/descendant::table/tr[6]/td[2]/a/text()").extract_first() 
        fund_fee = response.xpath("//div[@class='txt_cont']/descendant::table/tr[7]/td[1]/text()").extract_first()
        fund_trustee_fee = response.xpath("//div[@class='txt_cont']/descendant::table/tr[7]/td[2]/text()").extract_first()
        fund_service_fee = response.xpath("//div[@class='txt_cont']/descendant::table/tr[8]/td[1]/text()").extract_first() 
        fund_max_warrant_fee = response.xpath("//div[@class='txt_cont']/descendant::table/tr[8]/td[2]/text()").extract_first()
        fund_purchase_fee  = response.xpath("//div[@class='txt_cont']/descendant::table/td[1]/span[2]/span/text()").extract_first()
        fund_redemptin_fee = response.xpath("//div[@class='txt_cont']/descendant::table/td[2]/text()").extract_first() 
        fund_base_line = response.xpath("//div[@class='txt_cont']/descendant::table/tr[9]/td[1]/text()").extract_first()
        fund_trace = response.xpath("//div[@class='txt_cont']/descendant::table/tr[9]/td[2]/text()").extract_first()
        detailItem = fundDetailItem(fund_name=fund_name, fund_abbreviated_name=fund_abbreviated_name, \
                         fund_id=fund_id, fund_type=fund_type, fund_issue_date=fund_issue_date, \
                         fund_issue_date=fund_issue_date, fund_start_date=fund_start_date, \
                         fund_scale=fund_scale, fund_welfare=fund_welfare, fund_manager=fund_manager, \
                         fund_trustee=fund_trustee, fund_handler=fund_handler, fund_bonus=fund_bonus, \
                         fund_fee=fund_fee, fund_trustee_fee=fund_trustee_fee, \
                         fund_service_fee=fund_service_fee, fund_max_warrant_fee=fund_max_warrant_fee, \
                         fund_purchase_fee=fund_purchase_fee, fund_redemptin_fee=fund_redemptin_fee, \
                         fund_base_line=fund_base_line, fund_trace=fund_trace)
        yield detailItem
        value_link = self.allowed_domains[0] + url
        request = scrapy.Request(url=value_link, callback=self.parse_fund_value)
        request.meta['fund_value'] = True
        yield request

