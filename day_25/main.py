# # with open("data.csv") as file:
# #     data = file.readlines()
# #     print(data)

# # import csv

# # with open("data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #         print(temperatures)

import pandas as pn

data = pn.read_csv("data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)

# # # print(temp_list)
# # # print(data["temp"].max())
# # # print(data.temp.max())
# # print(data[data.temp == data.temp.max()])
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# # monday_temp = int(monday.temp)
# # monday_temp_F = monday_temp * 9/5 +32

# data_dict = {
#     "students": ["Amy", "James", "Angela" ],
#     "scores": [76, 56, 65]
# }
# data = pn.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

# import pandas

# data = pandas.read_csv("squirl_count.csv")

# color_list = data["Primary Fur Color"].to_list()
# #print(color_list)

# grey_squirls_count = len(data[data["Primary Fur Color"] == "Gray"])
# black_squirls_count = len(data[data["Primary Fur Color"] == "Black"])
# red_squirls_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

# squirl_dict = {
#     "Fur Color": ["Gray", "Black", "Cinnamon"],
#     "Count": [grey_squirls_count, black_squirls_count, red_squirls_count]
# }

# print(squirl_dict)
# df = pandas.DataFrame(squirl_dict)
# df.to_csv("squirl_colors.csv")
#print(squirl_colors_list)
# gray = data["Primary Fur Color" == "Gray"]
# print(gray)