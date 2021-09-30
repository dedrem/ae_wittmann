
def calculate_average_grade(grades):
    sum = 0
    for x in grades:
        sum += x
    return sum/len(grades)

def calculate_number(number):
    number *= 2
    number += 10
    number /= 2
    return number
