class dictionary_iter:

    def __init__(self, d: dict):
        self.d = d
        self.length = len(d)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.length:
            key = list(self.d.keys())[self.i]
            value = self.d[key]
            self.i += 1
            return key, value
        raise StopIteration


result = dictionary_iter({1: '1', 2: '2'})
for x in result:
    print(x)