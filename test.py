import quandl
from iexfinance import Stock
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import os
from os.path import join, dirname
from dotenv import load_dotenv


def import_stock_data(stock1, stock2, stock3):
    style.use('fivethirtyeight')

    start = dt.datetime(2016, 1, 1)
    end = dt.datetime(2018, 12, 31)
    stock_1_data = web.DataReader(stock1, 'yahoo', start, end)
    stock_2_data = web.DataReader(stock2, 'yahoo', start, end)
    stock_3_data = web.DataReader(stock3, 'yahoo', start, end)

    multi_df = pd.DataFrame({'stock1': stock_1_data['Adj Close'],
                             'Stock2': stock_2_data['Adj Close'],
                             'stock3': stock_3_data['Adj Close']})

    multi_df.plot()
    plt.legend()
    plt.show()


fb = 'fb'
import_stock_data('fb', 'tsla', 'GOOGL')
# style.use('ggplot')
# state = dt.datetime(2016, 1, 1)
# end = dt.datetime(2018, 12, 31)
# dotenv_path = join(dirname(__file__), 'apikey.env')
# load_dotenv(dotenv_path)
# alpha = os.getenv('ALPHAVANTAGE_API_KEY')
# # print(alpha)
# #
# df = web.DataReader('FB', 'av-daily', state, end, access_key=alpha)
# print(df.head())
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# print(df.head())
# # df.plot()
# # plt.show()
#
# ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
#
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])
# plt.show()

# tsla = Stock('TSLA')
# tsla.get_open()
# print(tsla.get_price())

# mydata = quandl.get("FRED/GDP")
# print(mydata)
