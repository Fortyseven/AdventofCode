#!/usr/bin/env python3

# from day3sample import input_data
from day3data import input_data

data_width = len(input_data[0])
column = [(0, 1)] * data_width

gamma = ""
eps = ""

for col in range(data_width):
    ones = 0
    zeroes = 0

    # iterate the data, extract the column
    for data_row in input_data:
        if data_row[col] == '1':
            ones += 1
        else:
            zeroes += 1

    if (ones > zeroes):
        gamma += '1'
        eps += '0'
    else:
        gamma += '0'
        eps += '1'

# print("gamma", int(gamma, 2))
# print("eps", int(eps, 2))
print("total", int(gamma, 2) * int(eps, 2))
