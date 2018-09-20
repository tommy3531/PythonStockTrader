import datetime as dt
from matplotlib import style
import pandas_datareader.data as web


def get_yahoo_stock_data(stock1, stock2, stock3):
    start = dt.datetime(2016, 1, 1)
    end = dt.datetime.now()
    stock_1_data = web.DataReader(stock1, 'yahoo', start, end)
    stock_2_data = web.DataReader(stock2, 'yahoo', start, end)
    stock_3_data = web.DataReader(stock3, 'yahoo', start, end)

    stock_tuple = (stock_1_data, stock_2_data, stock_3_data)

    return stock_tuple


def get_yahoo_single_stock(stock_name):
    start = dt.datetime(2016, 1, 1)
    end = dt.datetime.now()

    stock_data = web.DataReader(stock_name, 'yahoo', start, end)

    return stock_data


def yahoo_moving_average(df):
    """

    Take a window of time and calculate the average price in that window. Then shift that window
    over one period, and do it again.  Take the current price and the prices from the past 99 days
    add them up and divide by 100.  Then move the windown over 1 day and do the same thing over again.
    """

    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

    return df
