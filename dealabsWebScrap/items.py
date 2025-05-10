import scrapy

class DealabswebscrapItem(scrapy.Item):
    product_name = scrapy.Field()
    price = scrapy.Field()
    original_price = scrapy.Field()
    discount = scrapy.Field()
    link = scrapy.Field()
    date_posted = scrapy.Field()
    merchant = scrapy.Field()
    comments = scrapy.Field()  # Liste des commentaires
    votes = scrapy.Field()  # Votes positifs/négatifs