# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"You called {function.__name__} with args: {args} and kwargs: {kwargs}.\nIt returned: {result}"
    return wrapper



# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)

result = a_function(1, 2, 3)
print(result)