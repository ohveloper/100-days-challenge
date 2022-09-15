# List Comprehension

# 절차지향 코드
# numbers = [1, 2, 3]
# new_list = []
# for n in list:
#     add_1 = n + 1
#     new_list.append(add_1)

# list comprehension
# sample
# new_list = [new_item for item in list]

# 실사용
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = "Minkyo"
new_list_str = [letter for letter in name]
print(new_list_str)

new_numbers = [number * 2 for number in range(1,5)]
print(new_numbers)

## Conditional List Comprehension
# new_list = [new_item for item in list if test]

# test`1
names = ["hello", "world", "computer", "water", "pen"]
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(upper_names)

# test`2
check_list = [{"name":"jack", "check": 1}, {"name":"holland", "check": 0}]
test_list = [i["name"] for i in check_list if i["check"] == 1]
print(test_list)

