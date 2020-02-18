import scrapy

class NationSportsSpider(scrapy.Spider):
    name = "NationSports"

    start_urls = [
        # "https://www.nation.co.ke/sports/athletics/Fancy-Chemutai-fancies-her-chance-owning-a-world-record/1100-5457118-56ihf2z/index.html"
        # "https://www.nation.co.ke/sports/athletics/Brigid-Kosgei-set-for-first-race-of-season/1100-5459334-3l540t/index.html"
    ]

    def parse(self, response):
        for article in response.css("div.story-view"):
            yield {
                'title': article.css("header > h2::text").extract_first(),
                'publication_date': article.css("header > h6::text").extract_first(),
                'author': article.css("section.body-copy > section.author > strong::text").extract_first(),
                'body': article.css("section.body-copy > div > p::text").getall()
            }
