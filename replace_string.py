import re as re

def replace_string(df, series, bad_string, desired_string):
    """_summary_

    Args:
        df (_pandas.core.frame.DataFrame_): _the DataFrame you are performing operations on_
        series (_str_): _the series you are performing operations on_
        bad_string (_str_): _a string appearing in any cell whose contents you want to be replaced_
        desired_string (_str_): _the string you want_

    Returns:
        _pandas.core.frame.DataFrame_: _sets value of any cells containing the undesired string to the value of desired_string_
    """
    return df[series].str.replace(r"^.*"+bad_string+".*$", desired_string, regex=True, flags=re.IGNORECASE) 