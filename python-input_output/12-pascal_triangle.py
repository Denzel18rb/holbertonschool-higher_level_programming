#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """returns pascal triangle of size n"""
    if n <= 0:
        return []
    else:
        pascal = [[1]]

        for i in range(1, n):
            row = []
            row.append(1)
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])

            row.append(1)
            pascal.append(row)
            prev = row
        return pascal
