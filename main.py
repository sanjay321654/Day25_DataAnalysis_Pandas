# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

weather_data = pandas.read_csv("weather_data.csv")
# print(weather_data.to_dict())

# data = weather_data["temp"].tolist()

# avg_data = sum(data) / len(data)
# print(avg_data)

# print(weather_data["temp"].mean())
# print(weather_data["temp"].max())

# Get data in columns
# print(weather_data["condition"])
# print(weather_data.condition)

# Get data in rows
# print(weather_data[weather_data.day == "Monday"])

# Get data in row, which temperature is highest.
# print(weather_data[weather_data.temp == weather_data.temp.max()])

# monday = weather_data[weather_data.day == "Monday"]
# print(monday.condition)

# Create a data frame from scratch.
data_dict = {
    "students": ["sanjay", "praba", "kash"],
    "scores": [75, 99, 80]
}
data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("data.csv")
