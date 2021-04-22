##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## get_matrice.py
##

from sys import argv as av
from math import sqrt

def get_matrice():
    size_matrice = int(sqrt(len(av) - 2))
    n = 2

    matrice = []
    for x in range(size_matrice):
        matrice.append([])
        for i in range(size_matrice):
            matrice[x].append(int(av[n]))
            n += 1
    return matrice