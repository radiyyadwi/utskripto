from Function import *
import sys
import csv

filename = str(input("Nama file sumber: "))
filename_enc = str(input("Nama file terenkrip: "))

l = [0]*256
for i in read_input_bytes(filename):
    l[i] += 1

temp_dict = {}
for i in range(256):
    temp_dict[i] = l[i]

e = [0]*256
for i in read_input_bytes(filename_enc):
    e[i] += 1

temp_dict_enc= {}
for i in range(256):
    temp_dict_enc[i] = e[i]

print(l)
print(e)

with open('test.csv', mode='w+') as count_char:
    fieldnames = [i for i in range(256)]
    writer = csv.DictWriter(count_char, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(temp_dict)
    writer.writerow(temp_dict_enc)