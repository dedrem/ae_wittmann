import standard_lib
from aufgaben import *

if __name__ == "__main__":
    print("UE_6")

    print("\nsum up cart")
    item_prices = [2.04, 3.22, 5.66, 10, "wtwt"]
    standard_lib.print_f_string(cart_answer, item_prices, list_sum(item_prices))

    print("\ncreate a price list")
    article_name = "Leuchtdiode"
    article_price = 69.21
    print(create_price_list(article_name, article_price))

    print("\nshelferhelver")
    shelf = ["Transistor", "leer", "Leuchtdiode", "Fotodiode", "leer"]
    print(shelf)
    print(add_shelf(shelf, "Relais"))

    print("\npalindoomer")
    str_to_check = "Lagerkdkregal"
    standard_lib.print_f_string(palindrome_answer, str_to_check, "ein" if palindrome(str_to_check) else "kein")






