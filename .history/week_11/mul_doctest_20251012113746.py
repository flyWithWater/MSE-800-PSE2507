
def add(a:int,b:int)-> int:
    """
    >>> add(1,5)
    6
    >>> add(-9,9)
    0
    >>> add(5.5,4.5)
    10
    >>> add(0,0)
    0

    """
    return a+b

def subtraction(a:int,b:int)->int:
    """
    
    doctest part:
    >>> subtraction(-10,10)
    -20

    >>> subtraction(0,10)
    -10

    >>> subtraction(100,0)
    100
    

    """

    return a-b

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