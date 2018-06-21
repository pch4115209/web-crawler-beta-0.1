import scrapy

class WebSpider(scrapy.Spider):
    name = 'WorldCupBetCrawler'
    start_urls = ['https://www.sportsbet.com.au/betting/soccer/world-cup-2018/world-cup-matches?QuickLinks']

    def parse(self, response):
        print('======================================START===========================================')
        for game_list in response.css('ul.accordion-main'):
            match_name  = game_list.css('a ::text').extract_first()
            rates       = game_list.css('div.market-buttons .price-link')
            print(match_name)

            for rate in rates:
                print( rate.css('span.odd-val::text').extract_first() )

            #yield {'title': title.css('span.odd-val').extract_first()}

        print('======================================FINISH===========================================')

        #for next_page in response.css('div.prev-post > a'):
            #yield response.follow(next_page, self.parse)