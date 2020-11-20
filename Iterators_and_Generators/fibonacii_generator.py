def fibonacci():
    i, j = 0, 1
    while True:
        yield i
        i, j = j, i + j


generator = fibonacci()
for i in range(10):
    print(next(generator))