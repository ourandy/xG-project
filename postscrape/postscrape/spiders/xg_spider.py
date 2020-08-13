import scrapy
import pandas as pd
import numpy as np


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

        x = x.fillna(value=np.nan)

        x.dropna(

            axis=0,
            how='all',  # use 'any' if you want remove rows with even one empty value
            inplace=True

        )

        yield x.to_csv("xG.csv", sep=",", index=False)


# scrapy crawl expectedGoals --output exG.csv
