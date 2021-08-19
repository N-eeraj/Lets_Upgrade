import scrapy

class MySpider(scrapy.Spider):
    name = "PhoneSpider"
    start_urls = ["https://www.amazon.in/s?k=smartphone&crid=34N3IGRE3ELU3&sprefix=smartp%2Caps%2C844&ref=nb_sb_ss_ts-doa-p_1_6"]

    def parse(self, response, **kwargs):
        phone_names = response.css(".a-color-base.a-text-normal::text").extract()
        yield {"Name": phone_names}

        phone_rates = response.css(".a-price-whole::text").extract()
        yield {"Rate": phone_rates}