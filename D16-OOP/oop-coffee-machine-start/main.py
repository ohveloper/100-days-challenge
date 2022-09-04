from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
check_order = coffee_menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
  order = input(f"What would you like? ({check_order}): ")

  if order == "off":
    is_on = False
  
  elif order == "report":
    coffee_maker.report()
    money_machine.report()

  else:
    drink = coffee_menu.find_drink(order)
    is_okay_resource = coffee_maker.is_resource_sufficient(drink)
    is_okay_payment = money_machine.make_payment(drink.cost)

    if is_okay_resource and is_okay_payment:
        coffee_maker.make_coffee(drink)