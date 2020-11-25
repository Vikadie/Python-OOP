def cache(func):
    d = dict()

    def wrapper(arg):
        if arg not in d:
            res = func(arg)
            d[arg] = res
            return res
        return d[arg]

    setattr(wrapper, 'log', d)
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