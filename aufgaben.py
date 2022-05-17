from dataclasses import dataclass
from tkinter import N
import turtle
from winsound import Beep

# car
@dataclass
class car:
    color: str
    construction_year: int
    km_driven: float
    seats: int
    model: str

    def honk(self) -> None:
        print("möööööp")
        Beep(500,1000)

    def drive(self, km: float) -> None:
        print(f"{km} km driven")
        self.km_driven += km

    def park(self) -> None:
        print("parkingspot found")

    def get_km_driven(self) -> None:
        print(f"current km driven: {self.km_driven} km")

ferraroSportiglio: car = car(color="red", construction_year=1337, km_driven=14300, seats=69, model="sportycar")
ferraroSportiglio.honk()
ferraroSportiglio.get_km_driven()
ferraroSportiglio.drive(5)
ferraroSportiglio.get_km_driven()
ferraroSportiglio.park()


# fuel
mile = 1.609344
gallon = 3.785411784

def l100kmtompg(litres: float) -> float:
    range_in_miles = 100 / mile
    litres_in_gallon = litres / gallon
    return range_in_miles / litres_in_gallon

def mpgtol100km(miles: float) -> float:
    miles_in_km = miles * mile
    gallon_in_litre = gallon
    return (gallon_in_litre / miles_in_km) * 100


print(l100kmtompg(3.9), "should be 60.3114.....")
print(l100kmtompg(7.5), "should be 31.3619.....")
print(mpgtol100km(23.5), "should be 10.00913.....")
print(mpgtol100km(31.4), "should be 7.49091.....")



# prime numbers
def isPrime(number: int) -> bool:
    if number == 1 or number == 0:
        return None

    prime = True
    for i in range (2, number):
        if number % i == 0:
            prime = False

    return True if prime else None

# print(*[number for number in range(1, 101) if isPrime(number)], end=" ")


# sentence palindrom


def check_palindrom_sentence(sentence: str) -> bool:
    symbols = '".,!? '
    
    for symbol in symbols:
        sentence = sentence.replace(symbol, '')
    processed_sentence = sentence.lower()
    return processed_sentence == processed_sentence[::-1]


s = 'Mein ! isi "n"ieM!!'
print(check_palindrom_sentence(s), s)

def check_palindrom(sentence: str) -> bool:
    symbols = '".,!?'

    processed_sentence = sentence.lower()
    translation_symbols = processed_sentence.maketrans(symbols, '     ')
    processed_sentence = processed_sentence.translate(translation_symbols)
    processed_sentence = processed_sentence.replace(' ', '')
    return processed_sentence == processed_sentence[::-1]

print(check_palindrom(s), s)