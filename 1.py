from requests import Session
from os import system
session = Session()
clear = lambda: system("cls")


def uah_to_usd(amount):
    return round(float(session.get(
        "https://minfin.com.ua/currency/converter/uah-usd/"
    ).text.split('1 UAH = ')[1].split(' USD')[0])*amount, 2)


def usd_to_uah(amount):
    return round(float(session.get(
        "https://minfin.com.ua/currency/converter/uah-usd/"
    ).text.split('1 USD = ')[1].split(' UAH')[0])*amount, 2)


clear()
print("Currency Exchange\n\n1: UAH to USD\n2: USD to UAH\n")
system("title Currency Exchange")
asked = int(input("> "))
clear()
if asked in (1, 2):
    if asked == 1:
        print("How much UAH do you have?")
        asked = float(input("> "))
        clear()
        print(f"{asked} UAH = {uah_to_usd(asked)} USD")
        input("> ")
    elif asked == 2:
        print("How much USD do you have?")
        asked = float(input("> "))
        clear()
        print(f"{asked} USD = {usd_to_uah(asked)} UAH")
        input("> ")
else:
    print("Error: Please input 1 or 2")
    input("> ")
