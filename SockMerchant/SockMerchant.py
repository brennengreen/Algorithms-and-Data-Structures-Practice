#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()

    pair_count = 0
    current_color_value = ar[0]
    current_count = 0
    print("Initial Value:", current_color_value, ar)
    for color_value in ar:
        if color_value == current_color_value:
            current_count += 1
        else:
            print(color_value, current_count / 2)
            pair_count += int(current_count / 2)
            current_count = 1 # Reset current count while also adding the current value
            current_color_value = color_value

    pair_count += int(current_count / 2)

    return pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
