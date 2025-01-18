# Every function have docstrings and use strong typing 
def reverse_string(s: str) -> str:
    """
    Reverse the given string.
    Args:
    s (str): The input string to be reversed.
    Returns:
    str: The reversed string.
    """
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Count the number of vowels in the given string.
    Args:
    s (str): The input string to count vowels from.
    Returns:
    int: The number of vowels in the string.
    """
    vowels: str = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the given s
    tring.
    Args:
    s (str): The input string to capitalize.
    Returns:
    str: A new string with each word capitalized.
    """
    return ' '.join(word.capitalize() for word in s.split())