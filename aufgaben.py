from strings import *
import standard_lib
import locale

locale.setlocale(locale.LC_ALL, 'de_DE')


# sum over cart
def list_sum(prices: list) -> float:
    sum_cart = 0
    for item in prices:
        if isinstance(item, float) or isinstance(item, int):
            sum_cart += item
    return locale.currency(sum_cart)


# price table for article
def create_price_list(article_name: str, price: float) -> list:
    output = []
    for x in range(1, 11):
        output.append(standard_lib.create_f_string(price_table_line, x, article_name, locale.currency(x * price)))
    return output


# put item in virtual shelf
def add_shelf(shelf: list, item: str) -> list:
    shelf[shelf.index("leer")] = item
    return shelf


# check if a word is palindrome
def palindrome(word_to_check: str) -> bool:
    return word_to_check.lower() == word_to_check[::-1].lower()








