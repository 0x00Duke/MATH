##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-106bombyx-jose-antonio.rodriguez-assalone
## File description:
## err.py
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

def is_float(value):

    try:
        float(value)
    except ValueError:
        return False
    else:
        return True


def err():
    if len(av) == 2 and av[1] == "-h":
        return usage()
    elif not len(av) in [3, 4]:
        return usage()
    elif not is_int(av[1]) or int(av[1]) < 0:
        return usage()
    elif len(av) == 3 :
        if not is_float(av[2]) or (float(av[2]) < 1 or float(av[2]) > 4):
            return usage()
    elif len(av) == 4:
        if not is_int(av[2])  or not is_int(av[3]) or (int(av[2]) > int(av[3])) or int(av[2]) < 0:
            return usage()
    return 0