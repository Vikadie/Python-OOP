def make_bold(fn):
    def wrapper(*string):
        res = fn(*string)
        return f"<b>{res}</b>"
    return wrapper


def make_italic(fn):
    def wrapper(*string):
        res = fn(*string)
        return f"<i>{res}</i>"
    return wrapper


def make_underline(fn):
    def wrapper(*string):
        res = fn(*string)
        return f"<u>{res}</u>"
    return wrapper



@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))