#!/usr/bin/python3

import numpy as np

input_real_data_path = "real_data.txt"
input_test_data_path = "test_data.txt"

def import_data(inputFile):
    with open(inputFile, "r") as input_file:
        input_data = input_file.readlines()
    clean_data = []
    for line in input_data:
        clean_data.append(int(line.rstrip()))
    return clean_data


def custom_func(data):
    out = 0
    for x, y in zip(data[1:], data):
        out += (x-y) > 0 or 0
    return out

#part 1
data = import_data(input_real_data_path)
answer = custom_func(data)
print(answer)

#part 2
slid_avg = [(a + b + c) for a, b, c in zip(data, data[1:], data[2:])]
answer = custom_func(slid_avg)
print(answer)
