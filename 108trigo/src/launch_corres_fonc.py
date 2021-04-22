##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## launch_corres_fonc.py
##

from sys import argv as av

def launch_corres_fonc(math_fonc, matrice):
    for x in range(len(math_fonc)):
        if math_fonc[x].name == av[1]:
            return math_fonc[x].returning(matrice)