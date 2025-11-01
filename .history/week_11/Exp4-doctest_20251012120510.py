import doctest

"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

 
"""

# the function need to be test by the doctest.
def factorial(n):
    """
    The doctest code need to be in the comment part surrounded by \"\"\" and after the function declaration, not before the function declaration.
    The sign of the doctest is >>> in the comment, the frist line is just the calling code of the function. and then the second line is the expected result of the calling.

    """

    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    aa >>> factorial(34)
    2952327990396041408476186096435200000001
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":

    doctest.testmod()