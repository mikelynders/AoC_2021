#!/usr/bin/python3

import numpy as np


input_real_data_path = "real_data.txt"
input_test_data_path = "test_data.txt"

def import_data(inputFile):
    with open(inputFile, "r") as input_file:
        input_data = input_file.readlines()
    clean_data = []
    for line in input_data:
        clean_data.append([bool(int(x)) for x in line.rstrip()])
    return clean_data

data = import_data(input_real_data_path)
data = np.array(data)
inv_data = np.invert(data)
gamma_list = data.sum(axis=0)


inv_gamma_list = inv_data.sum(axis=0)
byte = np.where(gamma_list < inv_gamma_list, 0, 1)   
byte_inv = np.where(gamma_list < inv_gamma_list, 1, 0)   
gamma = int("".join(str(b) for b in byte), 2)

epsilon = int("".join(str(b) for b in byte_inv), 2)
print(gamma)
print(epsilon)
print(gamma*epsilon)

#part 2
o2_data = import_data(input_real_data_path)
count = 0
while len(o2_data) > 1:
    if len(o2_data) < 2:
        break
    first_col = np.rot90(o2_data)[::-1][count]
    rule = (np.count_nonzero(first_col)) >= len(first_col)/2
    to_remove = []
    for i, row in enumerate(first_col):
        if row != rule:
            to_remove.append(i)
    for r in to_remove[::-1]:
        o2_data.pop(r)
    count += 1
o2 = (int("".join(str(int(b)) for b in o2_data[0]), 2))
print(o2)

co2_data = import_data(input_real_data_path)
count = 0
while len(co2_data) > 1:
    if len(co2_data) < 2:
        break
    first_col = np.rot90(co2_data)[::-1][count]
    rule = (np.count_nonzero(first_col)) < len(first_col)/2
    to_remove = []
    for i, row in enumerate(first_col):
        if row != rule:
            to_remove.append(i)
    for r in to_remove[::-1]:
        co2_data.pop(r)
    count += 1
co2 = (int("".join(str(int(b)) for b in co2_data[0]), 2))

print(o2*co2)