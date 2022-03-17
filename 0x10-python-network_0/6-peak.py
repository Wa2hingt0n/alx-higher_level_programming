#!/usr/bin/python3
""" Defines a function find_peak """
def find_peak(list_of_integers):
    """ Returns the peak element in an unsorted list of integers """
    if list_of_integers == []:
        return None

    list_len = len(list_of_integers)
    if list_len == 1:
        return list_of_integers[0]
    elif list_len == 2:
        return max(list_of_integers[0], list_of_integers[1])

    m = int(list_len / 2)
    mid = list_of_integers[m]
    if mid > list_of_integers[m - 1] and mid > list_of_integers[m + 1]:
        return mid
    elif mid < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])
