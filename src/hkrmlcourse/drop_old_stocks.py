# drop_old_stocks.py

import pandas

def drop_old_stocks(stock_data: pandas.DataFrame,
                      threshold: int = 15000) -> pandas.DataFrame:
    """
    Drops stocks from a data frame downloaded from Yahoo Finance based on an
    age threshold, i.e. stocks that have data for more days than the
    threshold value are dropped. Default threshold is 15,000 days.

    :param stock_data: Stock data from Yahoo Finance.
    :type stock_data: pandas.DataFrame
    :param threshold: Maximum allowed number of days for which data can exist.
    :type threshold: int
    :return: A data frame without the dropped stocks.
    :rtype: pandas.DataFrame
    """
    ticker_ages = stock_data.Open.count()
    old_tickers = ticker_ages[ticker_ages > threshold].index

    return stock_data.drop(old_tickers, axis = 1, level = 1)
