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
    # TODO: print 수정
    coffee_maker.report()
    money_machine.report()
    # print("hello")

  else:
    # TODO: 이 아래로 전부 수정 정리 하기

    if coffee_maker.is_resource_sufficient(coffee_menu.find_drink(order)):
      if money_machine.make_payment(coffee_menu.find_drink(order).cost):
        coffee_maker.make_coffee(coffee_menu.find_drink(order))






# print(coffee_menu.find_drink("latte").name)
# print()