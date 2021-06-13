class Article:
    def __init__(self, article): # self, code, name, price
        article = article.split()
        self.code = article[0]
        self.name = article[1:-1]
        self.price = article[-1]
