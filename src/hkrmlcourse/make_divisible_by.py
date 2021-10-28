# make_divisible_by.py

import pandas

def make_divisible_by(input_data_frame: pandas.DataFrame,
                      divisor: int) -> pandas.DataFrame:
    """
    Removes the first rows of a data frame as to make the row number
    divisible by a desired number.

    :param input_data_frame: The input data frame.
    :type input_data_frame: pandas.DataFrame
    :param divisor: The desired divisor.
    :type divisor: int
    :return: A dataframe with a number of rows divisible by the divisor.
    :rtype: pandas.DataFrame
    """
    return input_data_frame[len(input_data_frame) % divisor]
