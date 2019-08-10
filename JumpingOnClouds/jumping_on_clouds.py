#!/bin/python3

import math
import os
import random
import re
import sys

def processJumps(c, i, jump_count):
    possible_jumps = c[i:i+3]
    print(possible_jumps, len(possible_jumps), jump_count)

    if (len(possible_jumps) == 1):
        return jump_count
    elif (len(possible_jumps) == 2):
        jump_count += 1
        return jump_count


    if possible_jumps[2] == 0:
        i += 2
        jump_count += 1
    elif possible_jumps[1] == 0:
        i += 1
        jump_count += 1
    
    if (i == len(c)):
        return jump_count


    return processJumps(c, i, jump_count)    

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    return processJumps(c, 0, 0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
