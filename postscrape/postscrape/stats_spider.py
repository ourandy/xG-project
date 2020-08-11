import scrapy
from scrapy.selector import Selector
import re

class PostSpider(scrapy.Spider):

    name = 'stats'

    start_urls = [
        'https://fbref.com/en/comps/12/stats/La-Liga-Stats',
    ]

    def parse(self, response):

        doc = response.xpath('//comment()').getall()

        doc_string = doc[11]

        re_string = doc_string.replace('<!--', '').replace('-->', '')

        selector = Selector(text=re_string, type="html")

        for row in selector.xpath('//*[@id="stats_standard"]//tbody/tr'):
            yield {
                'player': row.xpath('td[1]//text()').extract_first(),
                'nation': row.xpath('td[2]//text()').extract_first(),
                'position': row.xpath('td[3]//text()').extract_first(),
                'squad': row.xpath('td[4]//text()').extract_first(),
                'age':row.xpath('td[5]//text()').extract_first(),
                'born':row.xpath('td[6]//text()').extract_first(),
                'matches played':row.xpath('td[7]//text()').extract_first(),
                'starts':row.xpath('td[8]//text()').extract_first(),
                'minutes':row.xpath('td[9]//text()').extract_first(),
                'goals':row.xpath('td[10]//text()').extract_first(),
                'assists':row.xpath('td[11]//text()').extract_first(),
                'penalties':row.xpath('td[12]//text()').extract_first(),
                'penalties scored':row.xpath('td[13]//text()').extract_first(),
                'yellow cards':row.xpath('td[14]//text()').extract_first(),
                'red cards':row.xpath('td[15]//text()').extract_first(),
                'gls90':row.xpath('td[16]//text()').extract_first(),
                'ast90':row.xpath('td[17]//text()').extract_first(),
                'gls+ast90':row.xpath('td[18]//text()').extract_first(),
                'gls-pk90':row.xpath('td[19]//text()').extract_first(),
                'gls+ast-pk90':row.xpath('td[20]//text()').extract_first(),
                'xG':row.xpath('td[21]//text()').extract_first(),
                'noPenxG':row.xpath('td[22]//text()').extract_first(),
                'xA':row.xpath('td[23]//text()').extract_first(),
                'xG90':row.xpath('td[24]//text()').extract_first(),
                'xA90':row.xpath('td[25]//text()').extract_first(),
                'xG+xA90':row.xpath('td[26]//text()').extract_first(),
                'noPenxG90':row.xpath('td[27]//text()').extract_first(),
                'noPenxG+xA90':row.xpath('td[28]//text()').extract_first()
            }

        # with open("re_output.txt", "w") as text_file:
        #     text_file.write(re_string)

        # data = response.xpath('//comment()').extract()

        # up_data = []

        # for d in data:
        #     if 'key' in d:
        #         up_data.append(d)

        # html_template = '<html><body>%s</body></html>'

        # for up_d in up_data:
        #     up_d = html_template % up_d.replace('<!--', '').replace('-->', '')
        #     sel = Selector(text=up_d)
        #     sel.xpath('//div[@class="stats_standard"]')

        #     print(sel)

    # table = response.xpath('//*[@id="div_stats_standard"]/table')
    # print(table)

    #    for row in response.xpath('//*[@id="stats_standard"]//tbody/tr'):
    #        yield {
    #            'player': row.xpath('td[2]//text()').extract_first(),
    #            'nation': row.xpath('td[3]//text()').extract_first(),
    #            'pos': row.xpath('td[4]//text()').extract_first(),
    #            'squad': row.xpath('td[5]//text()').extract_first(),
    #            'age': row.xpath('td[6]//text()').extract_first(),
    #            'born': row.xpath('td[7]//text()').extract_first(),
    #            '90s': row.xpath('td[8]//text()').extract_first(),
    #            'att': row.xpath('td[9]//text()').extract_first(),
    #        }

    # div_stats_standard
    # div_stats_keeper
    # div_stats_keeper_adv
    # div_stats_shooting
    # div_stats_passing
    # div_stats_passing_types
    # div_stats_gca
    # div_stats_defense
    # div_stats_possession
    # div_stats_playing_time
    # div_stats_misc

    # div_stats_standard_squads
    # div_stats_keeper_squads
    # div_stats_keeper_adv_squads
    # div_stats_shooting_squads
    # div_stats_passing_squads
    # div_stats_passing_types_squads
    # div_stats_gca_squads
    # div_stats_defense_squads
    # div_stats_possession_squads
    # div_stats_playing_time_squads
    # div_stats_misc_squads

# scrapy crawl expectedGoals --output exG.csv

