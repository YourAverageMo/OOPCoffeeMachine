import os

from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

# ______TODOS_____
# -TODO print report
# -TODO check resources
# -TODO process coins
# -TODO check payment succ
# -TODO make coffee
# -TODO btw im basically making the same coffee machine over again so im not wasting time making it shiny like i did on the other one.


barista = CoffeeMaker()
menu = Menu()
cash_register = MoneyMachine()


def sclr():
    os.system("clear")


def main_menu():
    is_on = True
    while is_on:
        inventory = menu.get_items()
        order = input(f"What would you like to order today? {inventory}\n")
        if order == "off":
            print("shutting down. *whinning down noices*")
            return
        if order == "report":
            barista.report()
            cash_register.report()
            input("Press anything to continue...")
            sclr()
            continue
        drink = menu.find_drink(order)
        cost = drink.cost
        if barista.is_resource_sufficient(drink):
            print(
                f"\nCool! ill get your {drink.name} right our. Your total will be ${cost}\n")
            if cash_register.make_payment(cost):
                barista.make_coffee(drink)
                input("Press anything to continue...")
            else:
                print("Sorry, not enough cash")
                input("Press anyhing to continue...")
                sclr()
                continue
        else:
            input("Press anyhing to continue...")
        sclr()


sclr()
print("Good day sir. Im Caffine your barista for today!")
main_menu()
