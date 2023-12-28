"""
Util functions used for working with values that can be either a float or 'n/a'.

Functions:
    compare_with_na
    defaultdict_with_na

"""
from collections import defaultdict


def compare_with_na(a: str | int, b: str | int) -> str | int:
    """Return 'n/a' if a or b are 'n/a', else return a>b"""
    if isinstance(a, str) or isinstance(b, str):
        assert a == "n/a"

    if a == "n/a" or b == "n/a":
        return "n/a"
    if isinstance(a, float) and isinstance(b, float):
        return a > b

    raise ValueError("a, b must be either 'n/a' or floats")


def defaultdict_with_na(*args):
    """
    Same as python standard dict with one difference.
    If you try to access a key that does not exist it returns 'n/a' instead of throwing an error.
    """
    return defaultdict(lambda: "n/a", *args)
