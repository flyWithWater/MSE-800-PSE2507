
# this is a decorator of the function object
import time


def log_decorator(func):
    def wrapper(*args, **kwargs):
        #it is printing the original function's name and 
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        start_nanoseconds = int(round(time.time()*1000000))
        print(f"start_millis:{start_nanoseconds}")
        # this is a call of the original function, and result are just the result we get from the original function
        result = func(*args, **kwargs)
        end_nanoseconds = int(round(time.time()*1000000))

        execution_nanoseconds = end_nanoseconds-start_nanoseconds

        #func is just the object of the function . the syntax is printing its name and actual result from it.
        print(f"{func.__name__} executed {execution_nanoseconds} nanoseconds , returned {result}")
        return result
    return wrapper



@log_decorator
def add(a, b):
    return a + b



if __name__ == "__main__":
    add(3, 5)