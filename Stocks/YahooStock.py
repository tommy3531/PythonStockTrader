import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


def get_yahoo_stock_data(stock1, stock2, stock3):
    style.use('fivethirtyeight')

    start = dt.datetime(2016, 1, 1)
    end = dt.datetime(2018, 12, 31)
    stock_1_data = web.DataReader(stock1, 'yahoo', start, end)
    stock_2_data = web.DataReader(stock2, 'yahoo', start, end)
    stock_3_data = web.DataReader(stock3, 'yahoo', start, end)

    multi_df = pd.DataFrame({stock1: stock_1_data['Adj Close'],
                             stock2: stock_2_data['Adj Close'],
                             stock3: stock_3_data['Adj Close']})

    multi_df.plot()
    plt.legend()
    plt.show()
