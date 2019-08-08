#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    alt = 0 # Current altitude, 0 is sea level
    in_valley = False
    valley_count = 0

    for step in s:
        print(step, alt, in_valley)
        if step == 'U':
            alt += 1
            if alt >= 0 and in_valley:
                in_valley = False
                valley_count += 1
        if step == 'D':
            alt -= 1
            if alt < 0 and not in_valley:
                in_valley = True
    
        if alt >= 0 and in_valley:
            in_valley = False
            valley_count += 1
        elif alt < 0 and not in_valley:
            in_valley = True

    return valley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
