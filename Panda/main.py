# inbuilt method for working with csv
import csv

with open("Panda/weather_data - Sheet1.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for temp in data:
        if temp[1] != "temp":
            temperature.append(int(temp[1]))
            
    print(temperature)