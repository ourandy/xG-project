import scrapy


class PostSpider(scrapy.Spider):

    name = 'stats'

    start_urls = [
        'https://fbref.com/en/comps/12/stats/La-Liga-Stats',
    ]

    def parse(self, response):

        # table = response.xpath('//*[@id="div_stats_standard"]/table')
        # print(table)

       for row in response.xpath('//*[@id="stats_standard"]//tbody/tr'):
           yield {
               'player': row.xpath('td[2]//text()').extract_first(),
               'nation': row.xpath('td[3]//text()').extract_first(),
               'pos': row.xpath('td[4]//text()').extract_first(),
               'squad': row.xpath('td[5]//text()').extract_first(),
               'age': row.xpath('td[6]//text()').extract_first(),
               'born': row.xpath('td[7]//text()').extract_first(),
               '90s': row.xpath('td[8]//text()').extract_first(),
               'att': row.xpath('td[9]//text()').extract_first(),
           }

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
