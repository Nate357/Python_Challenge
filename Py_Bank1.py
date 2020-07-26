import csv
import os
import pandas as pd

budget = os.path.join("/Users/nathanuelmartin/Desktop/PyBank/budget_data.csv")

with open(budget) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')

    budget_header = next(budget_reader)
    print(budget_header)

    total_month = 0
    total_sum = 0
    change = 0
    previous = 0
    change_list = []
    greatest_inc = ["",0]
    greatest_dec = ["",9999]
    for row in budget_reader:

        total_month = total_month + 1
        total_sum = total_sum + int(row[1])
        change = int(row[1]) - previous
        previous = int(row[1])
        change_list.append(change)

        if change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = change

        if change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = change

    average_change = sum(change_list[1:])/(len(change_list)-1)

    print(total_month)
    print(total_sum)
    # print(change_list)
    print(average_change)
    print(greatest_inc[0],greatest_inc[1])
    print(greatest_dec[0],greatest_dec[1])
    

