# generate_appreciation_labels.py

import pandas

import hkrmlcourse.generate_multiindex

def generate_appreciation_labels(stock_history: pandas.DataFrame,
                                 shift_days: int = -1) -> pandas.DataFrame:
    """
    Takes a stock history data frame from Yahoo Finance and returns a data
    frame with boolean labels whether the stock appreciated the day after
    (with default settings).

    :param stock_history: Stock history from Yahoo Finance.
    :type stock_history: pandas.DataFrame
    :param shift_days: Number of days to shift labels (default -1).
    :type shift_days: int
    :return: A labels indexed by date and ticker symbols.
    :rtype: pandas.DataFrame
    """
    label_data_frame = stock_history.Close / stock_history.Open - 1 > 0
    shifted_data_frame = label_data_frame.shift(shift_days)

    column_titles = hkrmlcourse.generate_multiindex.generate_multiindex(
        shifted_data_frame,
        f"IntraDayAppreciation{abs(shift_days)}Day"
        f"{'s' if abs(shift_days) != 1 else ''}InThe"
        f"{'Future' if shift_days <= 0 else 'Past'}"
    )

    shifted_data_frame.columns = column_titles

    return shifted_data_frame
