import pandas

data = pandas.read_csv("Panda/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240619.csv")

gray = data[data["Primary Fur Color"] == "Gray"].shape[0]
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

new_data = {
    "fur Color": ["Gray","Cinnamon", "Black"],
    "count" : [gray, cinnamon, black ]
}
squirrel = pandas.DataFrame(new_data)
squirrel.to_csv("Panda/squirrel_count.csv")
print(new_data)