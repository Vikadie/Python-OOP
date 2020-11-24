def logged(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        return f"you called {fn.__name__}{args}\nit returned {res}"
    return wrapper

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))