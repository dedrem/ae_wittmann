from hello_world import *

print_variable("Hello World")
print_variable(123)

a = 5
b = 10
c = 20
d = 25

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
