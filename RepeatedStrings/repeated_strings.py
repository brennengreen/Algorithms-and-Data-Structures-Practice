#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count_of_a = 0
    for i in range(len(s)):
        if (s[i] == 'a'):
            count_of_a += 1
            print(count_of_a)

    num_of_reps = n // len(s)
    count_of_a = num_of_reps * count_of_a

    l = n % len(s)
    for i in range(l):
        if (s[i] == 'a'):
            count_of_a += 1

    return count_of_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
