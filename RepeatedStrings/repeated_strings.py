#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if s.count('a') == len(s):
        return n


    sub_string = ''
    while len(sub_string) < n:
        sub_string += s

    count = 0
    for c in sub_string[:n]:
        if c == 'a':
            count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
