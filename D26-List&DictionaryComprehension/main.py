# # List Comprehension
#
# # 절차지향 코드
# # numbers = [1, 2, 3]
# # new_list = []
# # for n in list:
# #     add_1 = n + 1
# #     new_list.append(add_1)
#
# # list comprehension
# # sample
# # new_list = [new_item for item in list]
#
# # 실사용
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
#
# name = "Minkyo"
# new_list_str = [letter for letter in name]
# print(new_list_str)
#
# new_numbers = [number * 2 for number in range(1,5)]
# print(new_numbers)
#
# ## Conditional List Comprehension
# # new_list = [new_item for item in list if test]
#
# # test`1
# names = ["hello", "world", "computer", "water", "pen"]
# short_names = [name for name in names if len(name) < 5]
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)
# print(upper_names)
#
# # test`2
# check_list = [{"name":"jack", "check": 1}, {"name":"holland", "check": 0}]
# test_list = [i["name"] for i in check_list if i["check"] == 1]
# print(test_list)
#
# # test 3
# with open("file1.txt") as f1:
#     f1_data = f1.readlines()
#
# with open("file2.txt") as f2:
#     f2_data = f2.readlines()
#     print(f2_data)
#
# result = [int(num) for num in f1_data if num in f2_data]
# print(result)
#
#
# # Dictionary Comprehension
# # sample
# # new_dict = {new_key:new_value for item in list}
# # new_dict = {new_key:new_value for (key, value) in dict.items()}
# # new_dict = {new_key:new_value for (key, value) in dict.items() if test}
#
# # test4
# students_name = ["hello", "world", "computer", "water", "pen"]
# import random
# students_scores = {student: random.randint(1,101) for student in students_name}
# print(students_scores)
#
# passed_students = {key:value for (key, value) in students_scores.items() if value > 60}
# print(passed_students)
#
# test2 = []


student_dict = {
    "student": ["Minkyo", "James", "Lily"],
    "score" : [65, 43, 85]
}

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

for key, row in student_data_frame.iterrows():
    print(row)
    row.score = 100
    print(row)


# {new_key: new_value for (index, row) in df.iterrows()}

### chellange

