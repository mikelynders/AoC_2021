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

data = import_data(input_test_data_path)
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
sub_bute = []
rule = [list(byte)]*len(data)
print(data)
print(rule)
output = np.where(data == rule, True, False)


print(data)
new_data = np.rot90(data)[::-1]
for rule_bit, data_row in zip(byte, new_data):
    print(rule_bit, data_row)
    for i, x in enumerate(data_row):
        if x != rule_bit:
            data[i][:] = None
    print("DATA", data)


