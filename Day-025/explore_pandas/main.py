
# #Using just file methods
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# #Using csv library
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# # Using the pandas library
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# # Get Row data value
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("Day-025/explore_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241201.csv")

gray_squrrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squrrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squrrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black" ],
    "Count" : [gray_squrrels_count, cinnamon_squrrels_count, black_squrrels_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("Day-025/explore_pandas/squrrel_count.csv")