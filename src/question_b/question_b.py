class Stock:

    def __init__(self, symbol, company_name) -> None:
        self.__symbol = symbol
        self.__company_name = company_name
    
    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    appl = Stock("APPL", "Apple inc")
    cat = Stock("CAT", "Caterpillar")
    ek = Stock("EK", "Eastman Kodak")
    goog = Stock("GOOG", "Google")
    msft = Stock("MSFT", "Microsoft")

    stock_dictionary = {
        "Apple Stock": appl,
        "Caterpillar Stock": cat,
        "Eastman Kodak Stock": ek,
        "Google Stock": goog,
        "Microsoft Stock": msft
    }

    print("Stock name - Company Name")
    for i in stock_dictionary:
        stock = stock_dictionary[i]
        print(f"{stock.get_symbol()} --- {stock.get_company_name()}")