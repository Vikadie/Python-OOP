def type_check(type):
    def decorator(fn):
        def wrapper(*args):
            res = "Bad Type"
            if all([True if isinstance(a, type) else False for a in args]):
                res = fn(*args)
            return res
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))