import quandl
from iexfinance import Stock
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
state = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('TSLA', 'yahoo', state, end)
print(df.head(6))


# tsla = Stock('TSLA')
# tsla.get_open()
# print(tsla.get_price())

# mydata = quandl.get("FRED/GDP")
# print(mydata)

