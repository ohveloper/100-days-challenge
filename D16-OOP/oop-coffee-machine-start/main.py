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
    print(coffee_maker.report())
    print(money_machine.report())
    # print("hello")

  else:
    # TODO: 이 아래로 전부 수정 정리 하기
    # print("world")
    # print(coffee_menu.find_drink(order).ingredients)
    if CoffeeMaker().is_resource_sufficient(coffee_menu.find_drink(order)):
      # print("hello")
      if MoneyMachine().make_payment(Menu().find_drink(order).cost):
        CoffeeMaker().make_coffee(coffee_menu.find_drink(order))


      # CoffeeMaker().make_coffee(order)





# print(coffee_menu.find_drink("latte").name)
# print()