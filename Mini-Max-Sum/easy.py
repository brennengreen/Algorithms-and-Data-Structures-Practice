#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    sum_min_arr = []
    sum_max_arr = []
    
    for i,n in enumerate(arr):
        if i < 4:
            #print(n, "min")
            sum_min_arr.append(n)
        if i > (len(arr)-1) - 4:
            #print(n, "max")
            sum_max_arr.append(n) 

    #print(sum_min_arr, sum_max_arr)
    print("{min} {max}".format(min=sum(sum_min_arr), max=sum(sum_max_arr)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)