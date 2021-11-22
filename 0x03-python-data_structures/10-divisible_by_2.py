#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple_2 = []
    for i in my_list:
        if i % 2 == 0:
            multiple_2.append(True)
        else:
            multiple_2.append(False)
    return (multiple_2)
