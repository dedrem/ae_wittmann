from strings import *


# order price
def get_order_price() -> None:
    value = float(input("How much is the fish?"))
    discount: float = 0
    shipping: int = 0

    if value < 25:
        shipping += 5
    if value > 150:
        discount = value*0.1

    order_price = value + shipping - discount

    print(f"Order was valued at {value}. Total price is: {order_price}.")


# brutto / netto calculator
def get_brutto_from_netto(tax_in_percent: float) -> None:
    price = float(input("How much is the fish? "))
    cost = "{0:.2f}".format(price * (1+tax_in_percent/100))
    print(f"Price was: {price}, total cost is {cost}")


# zinsberechung
def calculate_moneeeeeys():
    deposit = float(input("How much moneeeeeys do you want to deposit? "))
    yyield = float(input("How high is your Yield? "))
    duration = int(input("How long in days? "))

    abc = (deposit * yyield * duration) / (100 * 360)
    total_amount = "{0:.2f}".format(deposit + abc)

    print(f"With a deposit of {deposit} and a yield of {yyield}% you get {total_amount} moneeeeys "
          f"from the bank in {duration} days.")


# get price from user
def get_price_from_user()-> float:
    inp = input("Please enter your amount: ")
    return float(inp.replace(",", "."))


# umsatz stammkunde
def get_total(is_regular: bool) -> float:

    price: float = get_price_from_user()
    discount = 0

    if is_regular:
        if price > 1_000:
            if price > 5_000:
                discount = 20
            else:
                discount = 10
        else:
            discount = 5
    else:
        if price > 2_000:
            if price > 10_000:
                discount = 10
            else:
                discount = 5
        else:
            discount = 0

    return price * (1-discount/100)
