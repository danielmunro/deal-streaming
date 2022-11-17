class DealService:
    def __init__(self):
        self.cache = {}  # todo use a database here

    def add_deal(self, product_price):
        sku = product_price.sku
        if sku not in self.cache:
            self.cache[sku] = []
        self.cache[sku].append(product_price)

    def find_deal(self, sku):
        if sku not in self.cache:
            return
        lowest_price = None
        for product_price in self.cache[sku]:
            if lowest_price is None or product_price.price < lowest_price.price:
                lowest_price = product_price
        return lowest_price
