##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## div_matrice.py
##

def div_matrice(div, matrice):
    for i in range(len(matrice)):
        for x in range(len(matrice[i])):
            matrice[i][x] /= div
    return matrice