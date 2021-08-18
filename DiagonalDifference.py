#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference/problem
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    ltr = 0
    rtl = 0
    for i in range(len(arr)):
        ltr = arr[i][i] + ltr
        rtl = arr[i][len(arr) - i - 1] + rtl
    return abs(ltr - rtl)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
