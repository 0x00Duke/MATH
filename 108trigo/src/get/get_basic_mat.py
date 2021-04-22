##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## get_basic_mat.py
##

def basic_mat(matrice):
    basic = []
    n = 0
    for y in range(len(matrice)):
        basic.append([])
        for x in range(len(matrice[y])):
            if x == n:
                basic[y].append(1)
            else:
                basic[y].append(0)
        n += 1
    return basic