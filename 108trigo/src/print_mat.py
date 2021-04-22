##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## print_mat.py
##

def print_matrice(matrice):
    x = 0
    y = 0
    while y != len(matrice):
        x = 0
        while x != len(matrice[y]) - 1:
            print("%.2f\t" % matrice[y][x], end="")
            x += 1
        print("%.2f\n" % matrice[y][x], end="")
        y += 1