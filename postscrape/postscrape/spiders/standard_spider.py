import scrapy
from scrapy.selector import Selector
import re
import pandas as pd
import numpy as np
from .utils import SpiderUtils


class PostSpider(scrapy.Spider):

    name = "standard_players"

    start_urls = [
        "https://fbref.com/en/comps/11/stats/Serie-A-Stats",
    ]

    def parse(self, response):

        doc = response.xpath("//comment()").getall()

        doc_string = doc[21]

        re_string = doc_string.replace("<!--", "").replace("-->", "")

        selector = Selector(text=re_string, type="html")

        columns = []
        for column_node in selector.xpath('//*[@id="stats_standard"]/thead/tr[2]/th'):
            column_name = column_node.xpath("./text()").extract_first()
            columns.append(column_name)

        stats = []

        for row in selector.xpath('//*[@id="stats_standard"]/tbody/tr'):
            match = {}
            suffixes = {}
            for column_index, column_name in enumerate(columns):
                if column_name not in suffixes:
                    suffixes[column_name] = 1
                    df_name = column_name
                else:
                    suffixes[column_name] += 1
                    df_name = f"{column_name}_{suffixes[column_name]}"

                if column_name == "Rk":
                    match[df_name] = row.xpath("./th/text()").extract_first()
                elif column_name == "Matches":
                    link_list = row.xpath("./td/a/@href").extract()
                    if not link_list:
                        match[df_name] = ""
                    else:
                        match[df_name] = link_list[3]
                else:
                    match[df_name] = row.xpath(
                        "./td[{index}]//text()".format(index=column_index)
                    ).extract_first()

            stats.append(match)

        df = pd.DataFrame(stats, columns=columns)

        su = SpiderUtils()

        final_df = su.clean_df(df)

        yield final_df.to_csv("test_players_suffix.csv", sep=",", index=False)
