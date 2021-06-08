import pandas as p
import plotly_express as px
import csv
import numpy as n

read_data = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/Size of TV,_Average time spent watching TV in a week (hours).csv")

figure = px.scatter(read_data, x="Size of TV", y="Average time spent watching TV in a week (hours)")

#figure.show()

def get_data_source(path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        file_list = list(reader)
        file_list.pop(0)
        size_of_tv = []
        average_time_spent = []
        for i in range(0, len(file_list)):
            tv_size = file_list[i][0]
            size_of_tv.append(int(tv_size))
            time_spent = file_list[i][1]
            average_time_spent.append(int(time_spent))
        #print(size_of_tv)
        #print(average_time_spent)
        return {"x" : size_of_tv, "y" : average_time_spent}

def find_correlation(data):
    correlation = n.corrcoef(data["x"], data["y"])
    print()
    print("The Coficient of correlation is " + str(correlation[0,1]) + ".")
    print()

data_source = get_data_source("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/Size of TV,_Average time spent watching TV in a week (hours).csv")

find_correlation(data_source)