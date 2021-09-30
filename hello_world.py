def print_variable(x):
    print(x)


def print_calculation(x, y, sign, result):
    print(f"Das Ergebnis von {x} {sign} {y} ist {result}!")


def calculate_average(array_age):
    sum = 0
    for x in array_age:
        sum += x
    return sum/len(array_age)


def calculate_average_standard_overload(*args):
    sum = 0
    for x in args:
        sum += x
    return sum/len(args)