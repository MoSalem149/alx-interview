#!/usr/bin/python3
'''
Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    func: pascal_triangle
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    args:
        <int: n> : number of rows (> 0)
    return:
        <list <of list>>
    '''
    if type(n) is not int and n < 0:
        return ([])
    row = []
    for i in range(n):
        row.append([])
        row[i].append(1)
        if (i > 0):
            for j in range(1, i):
                row[i].append(row[i - 1][j - 1] + row[i - 1][j])
            row[i].append(1)

    return (row)
