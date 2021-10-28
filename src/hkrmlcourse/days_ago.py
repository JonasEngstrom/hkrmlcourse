# days_ago.py

import datetime

def days_ago(number_of_days_ago: int) -> str:
    """
    Takes an integer and returns the date that many days back from today.

    :param number_of_days_ago: Number of days back.
    :type number_of_days_ago: int
    :return: A string with a date in ISO format.
    :rtype: str
    """
    delta_time = datetime.timedelta(days = number_of_days_ago)
    return_time = datetime.date.today() - delta_time
    return_string = return_time.isoformat()

    return return_string
