import scrapy
import pandas as pd
import numpy as np

from .utils import SpiderUtils

class XGSpider(scrapy.Spider):

    name = 'expectedGoals'

    start_urls = [
        'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures',
    ]

    def parse(self, response):

        matches = []

        for row in response.xpath('//*[@id="sched_ks_3232_1"]//tbody/tr'):

            match = {
                'home': row.xpath('td[4]//text()').extract_first(),
                'homeXg': row.xpath('td[5]//text()').extract_first(),
                'score': row.xpath('td[6]//text()').extract_first(),
                'awayXg': row.xpath('td[7]//text()').extract_first(),
                'away': row.xpath('td[8]//text()').extract_first()
            }

            matches.append(match)

        x = pd.DataFrame(
            matches, columns=['home', 'homeXg', 'score', 'awayXg', 'away'])

        df_cleaner = SpiderUtils()
        clean_df = df_cleaner.clean_df(x)

        yield clean_df.to_csv("xG.csv", sep=",", index=False)


# scrapy crawl expectedGoals --output exG.csv
