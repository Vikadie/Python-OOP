class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for n in args:
            result *= n
        return result

    @staticmethod
    def divide(*args):
        result = 1
        for n in args:
            if result > 1:
                result /= n
            else:
                result = n
        return result

    @staticmethod
    def subtract(*args):
        result = 0
        i = 0
        for n in args:
            if i == 0:
                result = n
            else:
                result -= n

            i += 1
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

calc = Calculator()
print(calc.add(5, 10, 4))
print(calc.multiply(1, 2, 3, 5))
print(calc.divide(100, 2))
print(calc.subtract(90, 20, -50, 43, 7))
