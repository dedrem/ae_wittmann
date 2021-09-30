
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


def get_name_from_email(email):
    return email.split("@")[0]


def get_name_from_provider(email):
    return email.split("@")[1].split(".")[0]


def join_elements_to_list(*args):
    list = []
    for x in args:
        list.append(x)
    return list


def join_elements(args, char):
    return char.join(args)


