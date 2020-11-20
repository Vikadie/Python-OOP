class sequence_repeat:

    def __init__(self, sequence, number: int):
        self.sequence = list(sequence)
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.number:
            idx = self.index % len(self.sequence)
            self.index += 1
            return self.sequence[idx]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()
result = sequence_repeat('abc', 2)
for item in result:
    print(item, end ='')

print()
result = sequence_repeat('abc', 8)
for item in result:
    print(item, end ='')