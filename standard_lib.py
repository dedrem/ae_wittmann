# contains all standard operations


# gets input from user
def user_input(prompt: str, datatype: type) -> any:
    inp = input(prompt)
    if datatype == str:
        return inp
    elif datatype == int:
        return int(inp)
    elif datatype == float:
        return float(inp)


# prints f string
def print_f_string(string_to_print: str, *args) -> None:
    substrings = string_to_print.split("{}")
    output = substrings.pop(0)
    i = 0
    while len(substrings) > 0:
        output += str(args[i]) + substrings.pop(0)
        i += 1
    print(output)


# create f string
def create_f_string(string_to_print: str, *args) -> str:
    substrings = string_to_print.split("{}")
    output = substrings.pop(0)
    i = 0
    while len(substrings) > 0:
        output += str(args[i]) + substrings.pop(0)
        i += 1
    return output


# sum up a list
def sum_list(list_to_sum: list) -> any:
    output = 0
    for item in list_to_sum:
        output += item
    return output



