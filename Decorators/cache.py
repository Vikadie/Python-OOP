def cache(func):
    d = dict()

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        d[args[0]] = res
        setattr(wrapper, 'log', d)
        return res
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)