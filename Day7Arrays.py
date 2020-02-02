#!/bin/python3

import math
import os
import random
import re
import sys


x = ''
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    for i in range(n):
        x += str(arr[-(i+1)])+' '
print(x)
