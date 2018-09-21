from tickersymbols.webscraper import get_symbols_from_url


def sp_500_symbols():
    print(get_symbols_from_url('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'))
