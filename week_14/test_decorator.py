





# this is a decorator of the function object
def log_decorator(func):
    def wrapper(*args, **kwargs):
        #it is printing the original function's name and 
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        # this is a call of the original function, and result are just the result we get from the original function
        result = func(*args, **kwargs)
        #func is just the object of the function . the syntax is printing its name and actual result from it.
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper



@log_decorator
def add(a, b):
    return a + b



if __name__ == "__main__":
    add(3, 5)