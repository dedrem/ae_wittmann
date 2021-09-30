from aufgaben import *

# Listen

grades = [1, 2, 3, 4, 2, 1, 1]
print(f"Der Notendurchschnitt beträgt {calculate_average_grade(grades)}.")

number = 5
print(f"[Kommazahl] Die Berechnung mit der Nummer {number} ergibt {calculate_number(number)}.")
print(f"[Ganzzahl] Die Berechnung mit der Nummer {number} ergibt {int(calculate_number(number))}.")


# Übungsaufgaben

email = "willy.wizard@zauberschule.de"
print(f"Der Kunde mit der Email {email} heißt {get_name_from_email(email)}.")

email = "info@helena-hexe.de"
print(f"Der Kunde mit der Email {email} heißt {get_name_from_provider(email)}.")

mail1 = "zarah.zauber@zauberberg.de"
mail2 = "info@trixie-trickser.com"
mail3 = "uwe_unhold@dunkelnetz.de"

kunden = join_elements_to_list(mail1, mail2, mail3)
print(f"Die Kundenliste mit der Länge {len(kunden)} ist {kunden}.")

zauberer = ["Buehnenzauberer", "magic.com"]
print(f"Die Email lautet {join_elements(zauberer, '@')}.")
