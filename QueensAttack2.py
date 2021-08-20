#!/bin/python3
# https://www.hackerrank.com/challenges/queens-attack-2/problem
import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def fillObstacle(obstacles, n):
    matrix = [ [0]*n for i in range(n)]
    for obstacle in obstacles:
        matrix[obstacle[0]-1][obstacle[1]-1] = 1
    return matrix


def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles = fillObstacle(obstacles, n)
    up = countUp(n, r_q, c_q, obstacles)
    down = countDown(n, r_q, c_q, obstacles)
    right = countRight(n, r_q, c_q, obstacles)
    left = countLeft(n, r_q, c_q, obstacles)
    upRight = countUpRight(n, r_q, c_q, obstacles)
    upLeft = countUpLeft(n, r_q, c_q, obstacles)
    downRight = countDownRight(n, r_q, c_q, obstacles)
    downLeft = countDownLeft(n, r_q, c_q, obstacles)
    return up + down + right + left + upRight + upLeft + downRight + downLeft


def hasObstacle(r_q, c_q, obstacles):
    # for i in range(len(obstacles)):
    #     if obstacles[i][0] == r_q and obstacles[i][1] == c_q:
    #         return True
    # return False
    if obstacles[r_q-1][c_q-1] == 1:
        return True
    else:
        return False


def countUp(n, r_q, c_q, obstacles):
    count = 0
    if r_q == n:
        return 0
    for i in range(r_q + 1, n + 1):
        if hasObstacle(i, c_q, obstacles):
            return count
        else:
            count = count + 1
    return count


def countDown(n, r_q, c_q, obstacles):
    count = 0
    if r_q == 1:
        return 0
    for i in range(r_q - 1, 0, -1):
        if hasObstacle(i, c_q, obstacles):
            return count
        else:
            count = count + 1
    return count


def countRight(n, r_q, c_q, obstacles):
    count = 0
    if c_q == n:
        return 0
    for i in range(c_q + 1, n + 1):
        if hasObstacle(r_q, i, obstacles):
            return count
        else:
            count = count + 1
    return count


def countLeft(n, r_q, c_q, obstacles):
    count = 0
    if c_q == 1:
        return 0
    for i in range(c_q - 1, 0, -1):
        if hasObstacle(r_q, i, obstacles):
            return count
        else:
            count = count + 1
    return count


def countUpRight(n, r_q, c_q, obstacles):
    count = 0
    if r_q == n or c_q == n:
        return 0
    column = c_q
    row = r_q
    while column < n and row < n:
        column = column + 1
        row = row + 1
        if hasObstacle(row, column, obstacles):
            return count
        else:
            count = count + 1
    return count


def countUpLeft(n, r_q, c_q, obstacles):
    count = 0
    if r_q == n or c_q == 1:
        return 0
    column = c_q
    row = r_q
    while column > 1 and row < n:
        column = column - 1
        row = row + 1
        if hasObstacle(row, column, obstacles):
            return count
        else:
            count = count + 1
    return count


def countDownLeft(n, r_q, c_q, obstacles):
    count = 0
    if r_q == 1 or c_q == 1:
        return 0
    column = c_q
    row = r_q
    while column > 1 and row > 1:
        column = column - 1
        row = row - 1
        if hasObstacle(row, column, obstacles):
            return count
        else:
            count = count + 1
    return count


def countDownRight(n, r_q, c_q, obstacles):
    count = 0
    if r_q == 1 or c_q == n:
        return 0
    column = c_q
    row = r_q
    while column < n and row > 1:
        column = column + 1
        row = row - 1
        if hasObstacle(row, column, obstacles):
            return count
        else:
            count = count + 1
    return count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(str(result) + '\n')
