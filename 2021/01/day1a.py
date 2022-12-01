#!/usr/bin/env python3
from day1data import input_data

ups = 0
downs = 0

prev = 0

for cur in input_data:
    if cur > prev:
        ups += 1
    if cur < prev:
        downs += 1
    prev = cur


print("  UPS:", ups)
print("DOWNS:", downs)
