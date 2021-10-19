from aufgaben import *


# age checker
check_age(25, 30)
check_age(30, 30)
check_age(31, 30)


# drinking checker
check_drinking_age(18, "usa")
check_drinking_age(21, "UsA")
check_drinking_age(30, "USA")

check_drinking_age(16, "DE")
check_drinking_age(18, "AUS")
check_drinking_age(30, "CAN")


# printing lists
company = ["Intel", "NVIDIA", "Qualcomm", "Infineon", "AMD", "Texas Instruments"]
print_list(company)


# dog age
print(f"Das Hundealter entspricht {calculate_dog_age()} Menschenjahren")


# Übung mit Kontinenten
continents = ["Afrika", "Antarktis", "Asien", "Australien", "Europa", "Amerika"]

print("\n\nAlle Kontinente: ")
print_continents(continents)
print("\n\nAlle bewohnte Kontinente:")
print_inhabited_continents(continents)

stuff = ["Asien", "Max", 101, "London", "Antarktis"]

print("\n\nNur Kontinente aus der Liste stuff:")
print_only_continents(stuff, continents)