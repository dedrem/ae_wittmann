# Checks if person age > 30
def check_age(age_to_check: int, age_limit: int) -> None:
    if age_to_check > age_limit:
        print(f"Die Person ist über {age_limit} Jahre alt.")
    else:
        print(f"Die Person ist nicht über {age_limit} Jahre alt.")
    return


# checks if person is allowed to drink
def check_drinking_age(age_to_check: int, country: str) -> None:
    if country.lower() == "usa":
        if age_to_check >= 21:
            print(f"Du bist {age_to_check} Jahre alt und wohnst in den USA, deswegen darfst du drinken!")
        else:
            print(f"Du bist {age_to_check} Jahre alt und wohnst in den USA, deswegen darfst  du NICHT drinken!")
    else:
        if age_to_check >= 18:
            print(f"Du bist {age_to_check} Jahre alt und wohnst NICHT in den USA, deswegen darfst du drinken!")
        else:
            print(f"Du bist {age_to_check} Jahre alt und wohnst NICHT in den USA, deswegen darfst  du NICHT drinken!")
    return


# prints given list. "for" is not recommended but whatever
def print_list(list_to_print: list) -> None:
    for x in range(0, 1):
        print(*list_to_print, sep="\n")
    return


# calculate dog age
def calculate_dog_age() -> int:
    dog_age = int(input("Wie alt ist ihr Hund in ganzen Jahren? "))
    if dog_age == 1:
        return 14
    elif dog_age == 2:
        return 22
    elif dog_age > 2:
        return 22 + (dog_age - 2)*5
    else:
        return None
    return


# Aufgaben mit Listen
def print_continents(continents: list) -> None:
    print(*continents)
    return


def print_inhabited_continents(continents: list) -> None:
    continents.remove("Antarktis")
    print_continents(continents)
    continents.append("Antarktis") # only for fixing list in test_center.py
    return


def print_only_continents(list_to_check: list, list_template: list) -> None:
    for item in list_to_check:
        if item in list_template:
            print(item)
    return


def print_number_of_continents(list_to_check: list, list_template: list) -> None:
    number_of_continents = 0
    for item in list_to_check:
        if item in list_template:
            number_of_continents += 1
    print(f"Die Anzahl der Kontinente in der Liste ist: {number_of_continents}")
    return
