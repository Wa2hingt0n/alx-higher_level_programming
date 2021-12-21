#!/usr/bin/python3
"""Defines a function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of integers representing the Pascal's triangle of n

    Returns: List of integers representing the Pascal's triangle
    """
    triangle = []
    if n <= 0:
        return []
    else:
        for i in range(n):
            if i == 0:
                triangle.append([1])
            elif i == 1:
                triangle.append([1, 1])
            else:
                triangle.append([1 for j in range(i + 1)])
                for k in range(1, len(triangle[i]) - 1):
                    triangle[i][k] = triangle[i - 1][k - 1] + triangle[i - 1][k]
    return triangle
