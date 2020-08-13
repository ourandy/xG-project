import scrapy
from scrapy.selector import Selector
import re
import pandas as pd
import numpy as np

from .utils import SpiderUtils

class PostSpider(scrapy.Spider):

    name = 'standard_players'

    start_urls = [
        'https://fbref.com/en/comps/11/stats/Serie-A-Stats',
    ]

    def parse(self, response):

        doc = response.xpath('//comment()').getall()

        doc_string = doc[21]

        re_string = doc_string.replace('<!--', '').replace('-->', '')

        print(doc_string)

        selector = Selector(text=re_string, type="html")

        stats = []

        for row in selector.xpath('//*[@id="stats_standard"]//tbody/tr'):
            player_stat = {
                'player': row.xpath('td[1]//text()').extract_first(),
                'nation': row.xpath('td[2]//text()').extract_first(),
                'position': row.xpath('td[3]//text()').extract_first(),
                'squad': row.xpath('td[4]//text()').extract_first(),
                'age': row.xpath('td[5]//text()').extract_first(),
                'born': row.xpath('td[6]//text()').extract_first(),
                'matches_played': row.xpath('td[7]//text()').extract_first(),
                'starts': row.xpath('td[8]//text()').extract_first(),
                'minutes': row.xpath('td[9]//text()').extract_first(),
                'goals': row.xpath('td[10]//text()').extract_first(),
                'assists': row.xpath('td[11]//text()').extract_first(),
                'penalties': row.xpath('td[12]//text()').extract_first(),
                'penalties_scored': row.xpath('td[13]//text()').extract_first(),
                'yellow_cards': row.xpath('td[14]//text()').extract_first(),
                'red_cards': row.xpath('td[15]//text()').extract_first(),
                'goals_per_90': row.xpath('td[16]//text()').extract_first(),
                'assists_per_90': row.xpath('td[17]//text()').extract_first(),
                'goals_and_assists_per_90': row.xpath('td[18]//text()').extract_first(),
                'goals_minus_pens_per_90': row.xpath('td[19]//text()').extract_first(),
                'goals_plus_assists_minus_pens_per_90': row.xpath('td[20]//text()').extract_first(),
                'xG': row.xpath('td[21]//text()').extract_first(),
                'npxG': row.xpath('td[22]//text()').extract_first(),
                'xA': row.xpath('td[23]//text()').extract_first(),
                'xG90': row.xpath('td[24]//text()').extract_first(),
                'xA90': row.xpath('td[25]//text()').extract_first(),
                'xG_plus_xA_90': row.xpath('td[26]//text()').extract_first(),
                'npxG90': row.xpath('td[27]//text()').extract_first(),
                'npxG_plus_xA90': row.xpath('td[28]//text()').extract_first()
            }

            stats.append(player_stat)

        df = pd.DataFrame(stats, columns=['player', 'nation', 'position', 'squad', 'age', 'born', 'matches_played', 'starts',
                                          'minutes', 'goals', 'assists', 'penalties', 'penalties_scored', 'yellow_cards', 'red_cards', 'goals_per_90', 'assists_per_90',
                                          'goals_and_assists_per_90', 'goals_minus_pens_per_90', 'goals_plus_assists_minus_pens_per_90', 'xG', 'npxG', 'xA', 'xG90',
                                          'xA90', 'xG_plus_xA_90', 'npxG90', 'npxG_plus_xA90'])

        df_cleaner = SpiderUtils()
        clean_df = df_cleaner.clean_df(df)

        yield clean_df.to_csv("serie_a_standard_players.csv", sep=",", index=False)

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
