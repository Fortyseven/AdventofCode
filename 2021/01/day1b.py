#!/usr/bin/env python3

from day1data import input_data
# from day1sample import input_data

ups = 0
downs = 0
prev = None

WINDOW_SIZE = 3

for i in range(WINDOW_SIZE, len(input_data)+1):
    window = []
    cur = 0
    for wo in range(-WINDOW_SIZE, 0):
        offs = wo + i
        if offs in range(0, len(input_data)):
            window.append(input_data[offs])

    window_total = sum(window)
    if (window_total):
        if prev is not None and prev != window_total:
            # print(window, window_total, i)
            if window_total > prev:
                ups += 1
                # print("\tUpped at index", i, "\tprev:", prev)
            if window_total < prev:
                downs += 1

        prev = window_total


print("  UPS:", ups)
# print("DOWNS:", downs)
