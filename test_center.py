from aufgaben import *

grades = [1, 2, 3, 4, 2, 1, 1]
print(f"Der Notendurchschnitt beträgt {calculate_average_grade(grades)}.")

number = 5
print(f"[Kommazahl] Die Berechnung mit der Nummer {number} ergibt {calculate_number(number)}.")
print(f"[Ganzzahl] Die Berechnung mit der Nummer {number} ergibt {int(calculate_number(number))}.")
