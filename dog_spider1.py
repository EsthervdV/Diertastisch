import scrapy


class DogSpider(scrapy.Spider):
    name = "dogs"

    start_urls = [
        'https://nl.wikipedia.org/wiki/Affenpinscher'
    ]

    def parse(self, response, **kwargs):
        page = response.url
        filename = 'dogbreeds.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
