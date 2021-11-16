from aufgaben import *

# age checker
print("\n\nAltersprüfung: ")
check_age(25, 30)

# drinking checker
print("\n\nSaufprüfung: ")
check_drinking_age(18, "usa")
check_drinking_age(18, "AUS")

# printing lists
print("\n\nListen ausgeben: ")
company = ["Intel", "NVIDIA", "Qualcomm", "Infineon", "AMD", "Texas Instruments"]
print_list(company)

# dog age
print("\n\nHundealter ermitteln: ")
age = calculate_dog_age()
if age is None:
    print("critical error")
else:
    print(f"Das Hundealter entspricht einem {age} Jahren alten Menschen")


# Übungsaufgabe Groß mit Kontinenten
continents = ["Afrika", "Antarktis", "Asien", "Australien", "Europa", "Amerika"]
stuff = ["Asien", "Max", 101, "London", "Antarktis"]

print("\n\nAlle Kontinente: ")
print_continents(continents)

print("\n\nAlle bewohnte Kontinente:")
print_inhabited_continents(continents)

print("\n\nNur Kontinente aus der Liste stuff:")
print_only_continents(stuff, continents)

print("\n\nAnzahl der Kontinente aus der Liste stuff:")
print_number_of_continents(stuff, continents)

test = ["HALLO", "TSCHÜSS", "KARTOFFEL", "BIRNE"]
print(*test)
