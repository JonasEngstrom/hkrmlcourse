# drop_young_stocks.py

import pandas

def drop_young_stocks(stock_data: pandas.DataFrame,
                      threshold: int = 3650) -> pandas.DataFrame:
    """
    Drops stocks from a data frame downloaded from Yahoo Finance based on an
    age threshold, i.e. stocks that have data for fewer days than the
    threshold value are dropped.

    :param stock_data: Stock data from Yahoo Finance.
    :type stock_data: pandas.DataFrame
    :param threshold: Minimum required number of days for which data exists.
    :type threshold: int
    :return: A data frame without the dropped stocks.
    :rtype: pandas.DataFrame
    """
    ticker_ages = stock_data.Open.count()
    young_tickers = ticker_ages[ticker_ages > threshold].index

    return stock_data.drop(young_tickers, axis = 1, level = 1)
