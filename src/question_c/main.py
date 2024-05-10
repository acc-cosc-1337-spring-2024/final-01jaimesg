from question_c import Stock

def main():

    stock = Stock("MSFT", "Microsoft")

    print(f"{stock.get_symbol()} --- {stock.get_company_name()}")

main()