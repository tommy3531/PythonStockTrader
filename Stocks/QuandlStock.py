import quandl

quandl.ApiConfig.api_key = "yUFZbvzHdDKSeaUxZEwx"


def get_quandl_stock_data():
    data = quandl.get("WIKI/FB")
    print(data)


def get_quandl_date_range():
    data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")
    print(data)

