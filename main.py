from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

coffee_maker.report()
my_money_machine.report()

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? ({options}): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    coffee_maker.report()
    my_money_machine.report()
  else:
    drink = menu.find_drink(choice)
    print(drink)





