import pandas as p
import plotly_express as px
import csv
import numpy as n

reader = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/cups of coffee vs hours of sleep.csv")

figure = px.scatter(reader, x = "Coffee in ml", y = "sleep in hours", size = "sleep in hours", size_max = 25)

#figure.show()


def get_data_source(path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        file_list = list(reader)
        file_list.pop(0)
        cups_of_coffee = []
        sleep = []
        for i in range(0, len(file_list)):
            tv_size = file_list[i][0]
            cups_of_coffee.append(int(tv_size))
            time_spent = file_list[i][1]
            sleep.append(int(time_spent))
        #print(cups_of_coffee)
        #print(sleep)
        return {"x": cups_of_coffee, "y": sleep}


def find_correlation(data):
    correlation = n.corrcoef(data["x"], data["y"])
    print()
    print("The Coficient of correlation is " + str(correlation[0, 1]) + ".")
    print()


data_source = get_data_source("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/cups of coffee vs hours of sleep.csv")

find_correlation(data_source)
