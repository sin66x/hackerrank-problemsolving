#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    alice_point = 0
    bob_point = 0
    for index in range(3):
        if a[index] > b[index]:
            alice_point = alice_point + 1
        elif a[index] < b[index]:
            bob_point = bob_point + 1
    return (alice_point, bob_point)


if __name__ == '__main__':
    
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
    