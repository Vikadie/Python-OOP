class take_skip:
    def __init__(self, step: float, count: int):
        self.step = step
        self.count = count
        self.init = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.init < self.count * self.step:
            to_return = self.init
            self.init += self.step
            return to_return
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)