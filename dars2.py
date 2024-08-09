from os import system
from colorama import init, Fore

system('clear')

init(autoreset=True)

try:
    son1 = int(input("son kiriting: "))
    amal = input("belgi kiriting (+, -, *, /): ")
    son2 = int(input("son kiriting: "))

    if amal == "+":
        print(Fore.GREEN + f"{son1} + {son2} = {son1 + son2}")
    elif amal == "-":
        print(Fore.GREEN + f"{son1} - {son2} = {son1 - son2}")
    elif amal == "/":
        print(Fore.GREEN + f"{son1} / {son2} = {son1 / son2}")
    elif amal == "*":
        print(Fore.GREEN + f"{son1} * {son2} = {son1 * son2}")
    else:
        print("BUNDAY AMAL JO'Q")

except ValueError:
    print(Fore.RED + "Qiymat noto'g'ri kiritilindi!")

except ZeroDivisionError:
    print(Fore.RED + "0 ga bo'lib bo'maydi jigarello")

finally:
    print(Fore.MAGENTA + "Ahror: Tugadi")
