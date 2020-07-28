import scrapy

class XGSpider(scrapy.Spider):

    name = 'expectedGoals'

    start_urls = [
        'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures',
    ]

    def parse(self, response):

        for row in response.xpath('//*[@id="sched_ks_3232_1"]//tbody/tr'):
            yield {
                'home': row.xpath('td[4]//text()').extract_first(),
                'homeXg': row.xpath('td[5]//text()').extract_first(),
                'score': row.xpath('td[6]//text()').extract_first(),
                'awayXg': row.xpath('td[7]//text()').extract_first(),
                'away': row.xpath('td[8]//text()').extract_first()
            }
