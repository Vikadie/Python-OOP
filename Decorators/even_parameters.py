def even_parameters(fn):
    def wrapper(*args):
        res = "Please use only even numbers!"
        if all([True if (isinstance(i, int) and i % 2 == 0) else False for i in args]):
            res = fn(*args)
        return res
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))