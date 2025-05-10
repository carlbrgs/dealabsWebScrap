import scrapy
from ..items import DealabswebscrapItem

class DealabsSpider(scrapy.Spider):
    name = "dealabs"

    def __init__(self, search_query=None, *args, **kwargs):
        super(DealabsSpider, self).__init__(*args, **kwargs)
        self.search_query = search_query
        self.start_urls = [
            f"https://www.dealabs.com/search?q={search_query}" if search_query else "https://www.dealabs.com/"
        ]

    def parse(self, response):
        print(f"Scraping URL: {response.url}")  # Afficher l'URL en cours de scraping

        # Sélectionner les offres
        deals = response.css("article.thread")
        print(f"Nombre d'offres trouvées : {len(deals)}")  # Afficher le nombre d'offres sur la page

        for deal in deals:
            # Extraire le lien de l'offre
            link = deal.css("strong.thread-title a::attr(href)").get()
            if link:
                # Suivre le lien pour scraper les détails sur la page de l'article
                yield response.follow(link, self.parse_offer)

    def parse_offer(self, response):
        # Extraire le contenu principal
        content = response.css("body").get()
        if content:
            print(f"Contenu de l'offre : {content}")  # Afficher le contenu brut pour déboguer
        else:
            print("Aucun contenu trouvé pour cette offre.")