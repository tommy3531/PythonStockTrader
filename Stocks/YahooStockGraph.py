import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style


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
