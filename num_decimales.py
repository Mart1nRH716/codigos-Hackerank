import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positives = 0
    negatives = 0 
    zeros = 0
    for i in arr:
        if i < 0:
            negatives += 1
        elif i > 0:
            positives += 1
        else:
            zeros += 1

    # print(f"{positives/len(arr):.{6}f}")
    # print(f"{negatives/len(arr):.{6}f}")
    # print(f"{zeros/len(arr):.{6}f}")
    

if __name__ == '__main__':
    

    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)