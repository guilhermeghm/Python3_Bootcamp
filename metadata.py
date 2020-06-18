from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I'm wrapper function"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together."""
    return x + y

print(add(10,30))

#It will show the correct information because of the @wraps(fn) in the wrapper function.
print(add.__doc__)
print(add.__name__)
help(add)
