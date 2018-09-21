from pandas_datareader.nasdaq_trader import get_nasdaq_symbols


def get_nasdaq_ticker_symbols():
    get_nasdaq_symbols()
    symbols = get_nasdaq_symbols()
    print(dir(symbols))
    # print(symbols.loc['IBM'])
