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

from Stocks.YahooStock import get_yahoo_stock_data, get_yahoo_single_stock, yahoo_moving_average
from Stocks.YahooStockGraph import graph_yahoo_multi_stock, graph_yahoo_stock_high, graph_yahoo_moving_average

# data = get_yahoo_stock_data('fb', 'tsla', 'GOOGL')
# # print(data)
# graph_yahoo_multi_stock(data)
single_data = get_yahoo_single_stock('fb')
# graph_yahoo_stock_high(single_data)
df = yahoo_moving_average(single_data)
graph_yahoo_moving_average(df)












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
