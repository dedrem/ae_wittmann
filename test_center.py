from hello_world import *

print_variable("EIT11C UE 1")

a, b, c, d = 5, 10, 20, 25

addition = a+b
subtraction = d-c
multiplication = b*c
division = d/a

print_calculation(a, b, "+", addition)
print_calculation(d, c, "-", subtraction)
print_calculation(b, c, "*", multiplication)
print_calculation(d, a, "/", division)

ages = [17,18,29,10,25,30]
print(f"Das Durchschnittsalter der {len(ages)} Personen beträgt {calculate_average(ages)} Jahre.")
print(f"Das Durchschnittsalter der Personen beträgt {calculate_average_standard_overload(13,15,16,45,64)} Jahre.")

