##
## EPITECH PROJECT, 2020
## 108
## File description:
## error_check.py
##

from sys import argv as av
from src.usage import usage

def is_int(value):
    
    try:
        int(value)
    except ValueError:
        return False
    else:
        return True

def av_is_num():
    x = 2
    while x < len(av):
        if not is_int(av[x]):
            return 84
        x += 1
    return 0

def check_num_arg():
    len_arg = len(av) - 2
    i = 3
    sum_num = 1

    while sum_num < len_arg:
        sum_num += i
        i += 2
    return sum_num == len_arg

def error_check():
    if len(av) == 2 and av[1] == "-h":
        usage()
    if av_is_num() == 84:
        usage()
    if len(av) < 3 or not check_num_arg():
        usage()
    if not av[1] in ["EXP", "COS", "SIN", "COSH", "SINH"]:
        usage()