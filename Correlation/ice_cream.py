import pandas as p
import plotly_express as px
import csv
import numpy as n

reader = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")

figure = px.scatter(reader, x="Temperature", y="Ice-cream Sales( ₹ )", size = "Ice-cream Sales( ₹ )", size_max = 25)

#figure.show()

def get_data_source(path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        file_list = list(reader)
        file_list.pop(0)
        temp = []
        ice_cream_sales = []
        for i in range(0, len(file_list)):
            tv_size = file_list[i][0]
            temp.append(int(tv_size))
            time_spent = file_list[i][1]
            ice_cream_sales.append(int(time_spent))
        #print(temp)
        #print(ice_cream_sales)
        return {"x": temp, "y": ice_cream_sales}


def find_correlation(data):
    correlation = n.corrcoef(data["x"], data["y"])
    print()
    print("The Coficient of correlation is " + str(correlation[0, 1]) + ".")
    print()


data_source = get_data_source("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/Size of TV,_Average time spent watching TV in a week (hours).csv")

find_correlation(data_source)