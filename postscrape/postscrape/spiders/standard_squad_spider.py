import scrapy
from scrapy.selector import Selector
import re


class PostSpider(scrapy.Spider):

    name = 'standard_squad'

    start_urls = [
        'https://fbref.com/en/comps/11/stats/Serie-A-Stats',
    ]

    def parse(self, response):

        for row in response.xpath('//*[@id="stats_standard_squads"]//tbody/tr'):
            yield {
                'team': row.xpath('th/a/text()').extract_first(),
                'players_used': row.xpath('td[1]//text()').extract_first(),
                'possession': row.xpath('td[2]//text()').extract_first(),
                'played': row.xpath('td[3]//text()').extract_first(),
                'starts': row.xpath('td[4]//text()').extract_first(),
                'minutes': row.xpath('td[5]//text()').extract_first(),
                'goals': row.xpath('td[6]//text()').extract_first(),
                'assists': row.xpath('td[7]//text()').extract_first(),
                'penalties': row.xpath('td[8]//text()').extract_first(), 
                'penalties_scored': row.xpath('td[9]//text()').extract_first(),
                'yellow_cards': row.xpath('td[10]//text()').extract_first(),
                'red_cards': row.xpath('td[11]//text()').extract_first(),
                'goals_per_90': row.xpath('td[12]//text()').extract_first(),
                'assists_per_90': row.xpath('td[13]//text()').extract_first(),
                'goals_and_assists_per_90': row.xpath('td[14]//text()').extract_first(),
                'goals_minus_pens_per_90': row.xpath('td[15]//text()').extract_first(),
                'goals_plus_assists_minus_pens_per_90': row.xpath('td[16]//text()').extract_first(),
                'xG': row.xpath('td[17]//text()').extract_first(),
                'npxG': row.xpath('td[18]//text()').extract_first(),
                'xA': row.xpath('td[19]//text()').extract_first(),
                'xG90': row.xpath('td[20]//text()').extract_first(),
                'xA90': row.xpath('td[21]//text()').extract_first(),
                'xG_plus_xA_90': row.xpath('td[22]//text()').extract_first(),
                'npxG90': row.xpath('td[23]//text()').extract_first(),
                'npxG_plus_xA90': row.xpath('td[24]//text()').extract_first()
            }
