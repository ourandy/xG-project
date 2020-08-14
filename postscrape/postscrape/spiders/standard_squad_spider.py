import scrapy
from scrapy.selector import Selector
import re
import pandas as pd

class PostSpider(scrapy.Spider):

    name = "standard_squads"

    start_urls = [
        "https://fbref.com/en/comps/11/stats/Serie-A-Stats",
    ]

    def parse(self, response):

        column_index = 1
        columns = {}
        for column_node in response.xpath('//*[@id="stats_standard_squads"]/thead/tr[2]/th'):
            column_name = column_node.xpath("./text()").extract_first()
            print("column name is: " + column_name)
            columns[column_name] = column_index
            column_index += 1
            
            matches = []

        for row in response.xpath('//*[@id="stats_standard_squads"]/tbody/tr'):
            match = {}
            for column_name in columns.keys():

                if column_name=='Squad':
                    match[column_name]=row.xpath('th/a/text()').extract_first()
                else:
                    match[column_name] = row.xpath(
                        "./td[{index}]//text()".format(index=columns[column_name]-1)
                    ).extract_first()

            matches.append(match)
        
        print(matches)

        df = pd.DataFrame(matches,columns=columns.keys())

        yield df.to_csv("test.csv",sep=",", index=False)