from strings import *
import standard_lib
import math
import locale

locale.setlocale(locale.LC_ALL, "de_DE")


class ThreeDimensionalBody:
    def surface(self) -> float:
        pass

    def volume(self) -> float:
        pass


class Cube(ThreeDimensionalBody):
    def __init__(self, length_side):
        self.length_side = length_side

    def surface(self) -> float:
        return self.length_side ** 2

    def volume(self) -> float:
        return self.length_side ** 3


class Sphere(ThreeDimensionalBody):
    def __init__(self, radius):
        self.radius = radius

    def surface(self) -> float:
        return 4 * math.pi * self.radius**2

    def volume(self) -> float:
        return (3/4) * math.pi * self.radius**3


class Account:
    def __init__(self, credits, pin):
        self.credits: float = credits
        self.pin = pin

    def pay_in(self, amount) -> None:
        self.credits += amount

    def withdraw(self, amount) -> None:
        if not self.check_pin():
            print(error_message_pin)
        else:
            if amount > self.credits:
                standard_lib.print_f_string(error_message_money, locale.currency(self.credits))
            else:
                self.credits -= amount

    def check_pin(self) -> bool:
        user_input = standard_lib.user_input(pin_prompt, int)
        return True if user_input == self.pin else False



