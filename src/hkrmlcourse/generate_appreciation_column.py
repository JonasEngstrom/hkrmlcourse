# generate_appreciation_column.py

import pandas

import hkrmlcourse.generate_multiindex

def generate_appreciation_column(stocks: pandas.DataFrame) -> pandas.DataFrame:
    """
    Creates a column of intra day appreciation for data from Yahoo Finance.

    :param stocks: Stock history from Yahoo Finance.
    :type stocks: pandas.DataFrame
    :return: Appreciation indexed by date and ticker symbols.
    :rtype: pandas.DataFrame
    """
    appreciation = stocks.Close / stocks.Open - 1

    column_titles = hkrmlcourse.generate_multiindex.generate_multiindex(
        stocks,
        'IntraDayAppreciation'
    )

    appreciation.columns = column_titles

    return appreciation
