def solution(*args):
    def integers():
        i = 0
        while True:
            i += 1
            yield i

    def halves():
        for i in integers():
            yield i / 2

    def take(n , seq):
        lis = []
        for _ in range(n):
            lis.append(next(seq))
        return lis

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))