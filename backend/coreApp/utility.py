def convert_string_to_list(s: str, delimiter: str =',') -> list[str]:
    """
    The function `convert_string_to_list` takes a string and splits it into a list of substrings based
    on a specified delimiter.
    
    :param s: The parameter `s` is a string that you want to convert into a list by splitting it based
    on a specified delimiter
    :type s: str
    :param delimiter: The `delimiter` parameter in the `convert_string_to_list` function is used to
    specify the character or substring that separates the elements in the input string `s`. By default,
    the delimiter is set to `','`, which means that the input string will be split into a list of
    elements based on, defaults to ,
    :type delimiter: str (optional)
    :return: A list of strings is being returned, where the input string `s` has been split based on the
    specified delimiter.
    """
    return s.split(delimiter)

def check_none_or_empty(value: str) -> bool:
    """
    The function `check_none_or_empty` checks if a given string is either None or empty.
    
    :param value: The `check_none_or_empty` function takes a parameter `value` of type string and checks
    if it is either `None` or an empty string. If `value` is `None` or an empty string, the function
    returns `True`, otherwise it returns `False`
    :type value: str
    :return: The function `check_none_or_empty` returns a boolean value - `True` if the input `value` is
    either `None` or an empty string, and `False` otherwise.
    """
    if value is None or value == "":
        return True
    return False