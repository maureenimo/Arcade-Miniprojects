import pandas

data = pandas.read_csv("Panda/weather_data - Sheet1.csv")
data_dict = data.to_dict()
print(data_dict)
temperatures =  data["temp"].to_list()
print(data["temp"].mean())
max_temp = data["temp"].max()

# work with columns by treating them as a dictionary
data["temp"]
# work with columns by treating them as an object

print(data.day)
data.condition

# Get data from a row

print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
new_temp = (monday.temp * 9/5) + 32
print(f"The temperature was {new_temp}F")

# Create a dataframe from scratch
students = {
    "names":['Tulley', 'Chris', 'Mel'],
    "scores": [12,23,45]
}
newlist = pandas.DataFrame(students)
newlist.to_csv("Panda/student.csv")
print(newlist)

