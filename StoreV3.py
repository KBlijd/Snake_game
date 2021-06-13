from ReceiptClass import Receipt

CUSTOMER_SALES = open('store-sales.txt').read().split('=')


def store_handling(file):
    for sale in file:
        Receipt(sale).make_receipt()


store_handling(CUSTOMER_SALES)
