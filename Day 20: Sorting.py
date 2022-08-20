
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    
swap = 0
while a != sorted(a):
    for m in range(n-1):
        if a[m]> a[m+1]:
            swap += 1
            a[m],a[m+1]=a[m+1],a[m]

    

    
print("Array is sorted in {} swaps.".format(swap))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))




