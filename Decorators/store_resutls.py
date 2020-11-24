# class store_results:
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self, *args, **kwargs):
#         with open("results.txt", 'a+') as f:
#             res = self._func(*args, **kwargs)
#             f.write(f"Function '{self._func.__name__}' was called. Result: {res}\n")


def store_results(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        to_write = f"Function {fn.__name__} was called. Result: {res}\n"
        with open("results.txt", 'a+') as f:
            f.write(to_write)
    return wrapper


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)