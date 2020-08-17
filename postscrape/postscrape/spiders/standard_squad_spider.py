import scrapy
from scrapy.selector import Selector
import re
import pandas as pd

class PostSpider(scrapy.Spider):

    name = "squads"

    start_urls = [
        "https://fbref.com/en/comps/11/1896/misc/2018-2019-Serie-A-Stats",
    ]

    def parse(self, response):
        columns = []
        for column_node in response.xpath(
            '//*[@id="stats_misc_squads"]/thead/tr[2]/th'
        ):
            column_name = column_node.xpath("./text()").extract_first()
            columns.append(column_name)

        matches = []
        for row in response.xpath('//*[@id="stats_misc_squads"]/tbody/tr'):
            match = {}
            suffixes = {}
            for column_index, column_name in enumerate(columns):
                if column_name not in suffixes:
                    suffixes[column_name] = 1
                    df_name = column_name 
                else:
                    suffixes[column_name] += 1
                    df_name = f"{column_name}_{suffixes[column_name]}"

                if column_name == "Squad":
                    match[df_name] = row.xpath("th/a/text()").extract_first()
                else:
                    match[df_name] = row.xpath(
                        "./td[{index}]//text()".format(index=column_index)
                    ).extract_first()

            matches.append(match)

        df = pd.DataFrame(matches, columns=columns)

        yield df.to_csv("serie_a_misc_squads.csv", sep=",", index=False)

