# # with open("weather_data.csv") as data:
# #     # print(data.read())
# #     contents = data.read()
# #     # contents.readliens()
# #     data_list = contents.split("\n")
# #     print(data_list)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             # print(row[1])
# #             num_temperature = int(row[1])
# #             temperatures.append(num_temperature)
# #
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)     # Data Frame
# print(data["temp"])  # Series
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # temp_list 평균값 구하기
# added_temp = 0
#
# for temp in temp_list:
#       added_temp += temp
#
# ave_temp = added_temp / len(temp_list)
# print(round(ave_temp, 2))
#
# # ㅎㅎㅎ...
# ave = round(sum(temp_list) / len(temp_list), 2)
# print(ave)
#
# # ㅎㅎㅎㅎ..........평균 쉽네
# pd_ave = data["temp"].mean()
# print(pd_ave)
#
# # max
# pd_max = data["temp"].max()
# print(pd_max)
#
#
# # Get data in Columns
# print(data["condition"])
# print(data.condition)
#
#
# # Get Data in Row
# print(data[data.day == "Monday"])   # day row 중 Monday 체크
# print(data[data.temp == data["temp"].max()])    # 가장높은 온도를 가진 row 출력
#
# ## 그룹회고 짤때 좋겠다.
# monday = data[data.day != "Monday"]
# print(monday)
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # 섭씨 * 1.8 + 32 == 화씨
# monday = data[data.day == "Monday"]
# mon_temp = int(monday.temp)
# trans = mon_temp * 1.8 + 32
# print(trans)
# # monday.temp = trans
# # print(monday)
#
#
# # Create a dataframe from scratch
# students_data_dict = {
#       "students": ["Shay", "MK", "Neul"],
#       "score" : [77, 66, 55]
# }
#
# new_dataframe = pandas.DataFrame(students_data_dict)
# print(new_dataframe)
# new_dataframe.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_col = data["Primary Fur Color"]
# print(color_col.to_list())
unique_color_list = color_col.unique()

cnt_color_dict = {
    "Fur Color": [],
    "Count": []
}

for i in unique_color_list:
    # print(i)
    if type(i) is str:
        cnt = data[data["Primary Fur Color"] == i]
        # print(cnt)
        # print(len(cnt))
        cnt_color_dict["Fur Color"].append(i)
        cnt_color_dict["Count"].append(len(cnt))

print(cnt_color_dict)

new_dataframe = pandas.DataFrame(cnt_color_dict)
print(new_dataframe)
new_dataframe.to_csv("squirrel_count.csv")