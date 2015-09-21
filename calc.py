#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def to_number(num):
    try:
        if '.' in num:
            return float(num)
        else:
            return int(num)
    except:
        sys.exit("Error")

op1 = to_number(sys.argv[1])
operation = sys.argv[2]
op2 = to_number(sys.argv[3])

def sum(num1, num2):
    return num1 + num2
def substraction(num1, num2):
    return num1 - num2

if operation == "suma":
    print (sum(op1, op2))
elif operation == "resta":
    print (substraction(op1, op2))
else:
    print ("Not allowed operation ", operation)
