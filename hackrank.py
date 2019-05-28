import math
import os
import random
import re
import sys


def countingValleys(n, s):
    valley = 0
    sum = 0
    for direction in s:
        if direction == 'U':
            sum += 1
            if sum == 0:
                valley += 1
        elif direction == 'D':
            sum -= 1
    return(valley)


countingValleys(8, 'DDUUDDUU')
