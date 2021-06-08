from os import read
import pandas as p
import plotly_express as px
import csv
import numpy as n

read_data = p.read_csv("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/Student Marks vs Days Present.csv")

figure = px.scatter(read_data, x="Days Present", y="Marks (In Percentage)", size="Marks (In Percentage)", size_max = 25)

#figure.show()


def get_data_source(path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        file_list = list(reader)
        file_list.pop(0)
        student_marks = []
        days_present = []
        for i in range(0, len(file_list)):
            tv_size = file_list[i][0]
            student_marks.append(int(tv_size))
            time_spent = file_list[i][1]
            days_present.append(int(time_spent))
        #print(student_marks)
        #print(days_present)
        return {"x": student_marks, "y": days_present}


def find_correlation(data):
    correlation = n.corrcoef(data["x"], data["y"])
    print()
    print("The Coficient of correlation is " + str(correlation[0, 1]) + ".")
    print()


data_source = get_data_source("D:/(4) WhiteHatJr. Codes/Third Module/Correlation/csv files/Student Marks vs Days Present.csv")

find_correlation(data_source)
