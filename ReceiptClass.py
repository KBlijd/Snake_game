from ArticleClass import Article

OPENING_PHRASE = "****** Bert's Buurtwinkel ******"
LEFT_ALIGN_WORD = 'article'
RIGHT_ALIGN_WORD = 'price'

START_AMOUNT = 0
ROUNDING_DECIMALS = 2

TO_BE_PAID_SENTENCE = '>>>>>>>>>>>> to be paid:'
CLOSING_SENTENCE = '***** Thank you for your business *****'

ARTICLES = open('store-data.txt').read().splitlines()


def make_barcode_file(file):
    result = []
    for article in file:
        article = article.split()
        result.append(article[0])
    return result


barcode_file = make_barcode_file(ARTICLES)


class Receipt:
    def __init__(self, order):
        self.order = order.splitlines()
        # init price + words

    def make_receipt(self):

        print(OPENING_PHRASE)
        print(f'{LEFT_ALIGN_WORD:<30}{RIGHT_ALIGN_WORD:>30}')

        to_be_paid = START_AMOUNT

        for barcode in self.order:
            if barcode in barcode_file:
                for article in ARTICLES:
                    article = Article(article)
                    if article.code == barcode:
                        to_be_paid += float(article.price)
                        full_article_name = ''
                        for name_part in article.name:
                            full_article_name += name_part
                            full_article_name += ' '
                        print(f'{full_article_name:<30}{article.price:>30}')
            else:
                print(f'barcode: {barcode} not found in database')
        print(f'{TO_BE_PAID_SENTENCE}{round(to_be_paid, ROUNDING_DECIMALS)}')
        print(f'{CLOSING_SENTENCE} \n')
