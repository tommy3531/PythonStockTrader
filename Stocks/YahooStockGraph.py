import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc

def graph_yahoo_multi_stock(dataframe):
    style.use('fivethirtyeight')

    multi_df = pd.DataFrame({"stock1": dataframe[0]['Adj Close'],
                             "stock2": dataframe[1]['Adj Close'],
                             "stock3": dataframe[2]['Adj Close']})
    multi_df.plot()
    plt.legend()
    plt.show()


def graph_yahoo_stock_high(data_frame):
    style.use('fivethirtyeight')

    data_frame.reset_index(inplace=True)
    data_frame.set_index("Date", inplace=True)

    data_frame[['High', 'Low']].plot()
    plt.xlabel('Date')
    plt.ylabel('High and Low')
    plt.title('Stock data from 2016 to present')
    plt.legend()
    plt.show()


def graph_yahoo_moving_average(df):
    style.use('ggplot')

    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)

    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

    ax1.plot(df.index, df['Adj Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])

    plt.show()


def graph_yahoo_candlestick(df):
    style.use('ggplot')

    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)

    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

    df_ohlc = df['Adj Close'].resample('10D').ohlc()
    df_volume = df['Volume'].resample('10D').sum()
    print(df_ohlc.head())