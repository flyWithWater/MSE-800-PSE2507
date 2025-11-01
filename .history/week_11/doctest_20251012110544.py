

def mul(a: int, b: int) -> int:
    """
    >>> mul(0,9)
    0
    >>> mul(1,20)
    20
    >>> mul(8,10)
    80
    >>> mul(88,-1)
    -88

    """
    return a * b


if __name__ == "__main__":
    import doctest
    doctest.testmod()