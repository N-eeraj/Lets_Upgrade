import scrapy

class QuotesSpider(scrapy.Spider):
    name = "QuoteSpider"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
        title = response.xpath("//title/text()").extract()[0]
        yield {"Title": title}

        quotes = response.css(".text::text").extract()
        yield {"Quotes": quotes}