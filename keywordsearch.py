#!/usr/bin/env python
# coding: utf-8

import pandas as pd

data = pd.read_csv("data.csv")  # data.csv is the csv file provided

sub = input("Enter a word to search")  # we get a key from the user to search

data["medIndex"] = data["medName"].str.find(
    sub)  # finding the results with the key got from the user in the medName field
data["saltIndex"] = data["saltName"].str.find(
    sub)  # finding the results with the key got from the user in the saltName field
data["manufacturerIndex"] = data["manufacturer"].str.find(
    sub)  # finding the results with the key got from the user in the manufacturer field

count = -1  # variable to track the row
ctr = 0  # variable to track the number of results found
for med, salt, manuf, in zip(data["medIndex"], data["saltIndex"], data["manufacturerIndex"]):  # from the index found
    # we filter the positive ones and take the entire row as the result using this for loop
    count = count + 1  # traverse the row
    if med >= 0 or salt >= 0 or manuf >= 0:  # getting the positive results from the search
        ctr = ctr + 1  # increment the number of results found by 1
        print(ctr)  # prints the number of results
        print("Med Name-->" + data["medName"][count])  # prints the medName of the result row found
        print("Salt Name-->" + str(data["saltName"][count]))  # prints the saltName of the result row found
        print("Manufacturer-->" + str(data["manufacturer"][count]))  # prints the manufacturer of the result row found
        print("MRP-->" + str(data["mrp"][count]))  # prints the mrp of the result row found
        print("Best Price-->" + str(data["bestPrice"][count]))  # prints the best price of the result row found
        print("Pack Size-->" + str(data["packSize"][count]))  # prints the pack size of the result row found
