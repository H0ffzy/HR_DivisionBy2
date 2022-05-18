#!/bin/python

import math
import os
import random
import re
import sys


def isDivisibleBy2(num):
    if (num % 2) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    #n = int(raw_input().strip())
    n = int(18)

    if isDivisibleBy2(n):
        if n > 20:
            print("Not Weird")
        elif n <= 20 and n >= 6:
            print("Weird")
        elif n <= 5:
            print("Not Weird")
    else:
        print("Weird")