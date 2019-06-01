import math
import os
import random
import re
import sys

def rotLeft(a, d):
    outArr = []
    for num in range(len(a)):
        outArr.append(num)
    for index, number in enumerate(a):
       newIn = (index-d)
       outArr[newIn] = number
    return(outArr)

a = [1,2,3,4,5]
d = 4

rotLeft(a,d)
