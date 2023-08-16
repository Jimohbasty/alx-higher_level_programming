#!/usr/bin/python3

def uniq_add(my_list=[]):
    unq = set(my_list)
    sum = 0
    for i in unq:
        sum += i
    print(sum)
