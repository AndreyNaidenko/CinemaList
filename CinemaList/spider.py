import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'movies'
    start_urls = [
        'https://www.ivi.ru/movies/arthouse',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'genre': quote.css('li.top-menu__sublist-item::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)