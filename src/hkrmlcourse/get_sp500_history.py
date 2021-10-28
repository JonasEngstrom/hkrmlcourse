# get_sp500_history.py

import yfinance
import pandas
import variables

def get_sp500_history(tickers_to_import: str = variables.sp500_tickers,
                      start_date: str = '1900-01-01') -> pandas.DataFrame:
    """
    Returns a Pandas DataFrame with historical data for the S&P 500,
    downloaded from Yahoo Finance. Uses tickers from October 27th 2021,
    which can be overridden if the user so chooses.

    :param tickers_to_import: Ticker symbols, default set to S&P 500 companies.
    :type tickers_to_import: str
    :param start_date: Start date for retrieved data, default 1900-01-01.
    :type start_date: str
    :return: A Pandas DataFrame with historical data for the S&P 500.
    :rtype: Pandas.DataFrame
    """
    return yfinance.download(tickers_to_import, start = start_date)
