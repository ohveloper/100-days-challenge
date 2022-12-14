MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# TODO: 4. Check resources sufficient?
# TODO: for loop으로 바꿔보자
def check_resources(order, resources):
    for item in MENU[order]["ingredients"]:
        # print(item)
        if MENU[order]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# TODO: 5. Process coins.
def process_coins(order):
    quarters = round(int(input("quarters: ")) * 0.25, 3)
    dimes = round(int(input("dimes: ")) * 0.1, 3)
    nickles = round(int(input("nickles: ")) * 0.05, 3)
    pennies = round(int(input("pennies: ")) * 0.01, 3)
    # print(quarters, dimes, nickles, pennies)
    result = quarters + dimes + nickles + pennies
    # print(result)
    change = result - MENU[order]['cost']
    if result < MENU[order]['cost']:
        print(f"not enough money. sorry, here you go ${result}")
        return 0
    else:
        print(f"change: ${change}")
        return result - change

# TODO: 7. Make Coffee.
# TODO: for loop 으로 바꿔보자
def make_coffee(order):
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]

# TODO: resources 추가
def add_resources():
    return {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

Flag = True

# 실제 작동하는 구간
while Flag:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order = input('''What would you like? (espresso/latte/cappuccino): ''')

    # TODO: 2. Turn off the Coffee Machine by entering “​off”​to the prompt.
    if order == "off":
        Flag = False
        print("okay bye")
        break

    # TODO: 3. Print report.
    elif order == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}ml')
        print(f'Money: ${money}')

    # 재료 부족할때 한방에 채워넣는 함ㅅ
    elif order == "add":
        resources = add_resources()

    else:
        # 리소스 체크하고 리턴값 true, fasle 확인해서 괜찮으면
        if check_resources(order,resources):
            # 코인 확인하고
            check_coin = process_coins(order)
            # 코인 리턴값 0 아니면
            if check_coin != 0:
                #커피 만들고 돈통에 돈 추가하고 마무리
                make_coffee(order)
                money += check_coin
                print(f"Here is your {order}. Enjoy!")


# TODO: 6. Check transaction successful?