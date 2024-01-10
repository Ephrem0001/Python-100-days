import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(Cinnamon_squirrels)
print(Black_squirrels)

DATA_DICT = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, Cinnamon_squirrels, Black_squirrels]
}

df = pd.DataFrame(DATA_DICT)
df.to_csv("squirrel_count.csv")
