#!/usr/bin/python3
"""Defines a function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of integers representing the Pascal's triangle of n

    Returns: List of integers representing the Pascal's triangle
    """
    triang = []
    if n <= 0:
        return triang
    else:
        for i in range(n):
            if i == 0:
                triang.append([1])
            elif i == 1:
                triang.append([1, 1])
            else:
                triang.append([1 for j in range(i + 1)])
                for k in range(1, len(triang[i]) - 1):
                    triang[i][k] = triang[i - 1][k - 1] + triang[i - 1][k]
    return triang
