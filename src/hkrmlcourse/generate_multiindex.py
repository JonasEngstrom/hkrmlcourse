# generate_multiindex.py

import pandas

def generate_multiindex(sub_level_data_frame: pandas.DataFrame,
                        super_level: str) -> pandas.MultiIndex:
    """
    Returns a Pandas MultiIndex object with two levels. The superior level is
    defined by the parameter super_level and the inferior level is defined by
    the column names in the parameter sub_level_data_frame.

    :param sub_level_data_frame: Dataframe with column names for sub level.
    :type sub_level_data_frame: pandas.DataFrame
    :param super_level: Name of super level.
    :type super_level: str
    :return: A two level index.
    :rtype: pandas.MultiIndex
    """
    label_tuples = []

    for column_name in sub_level_data_frame.columns:
        label_tuples.append((super_level, column_name))

    return pandas.MultiIndex.from_tuples(label_tuples)
