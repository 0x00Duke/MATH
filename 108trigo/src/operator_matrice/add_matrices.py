##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## add_matrices.py
##

def add_matrices(mat_one, mat_two):
    for x in range(len(mat_one)):
        for i in range(len(mat_one[x])):
            mat_one[x][i] += mat_two[x][i]
    return mat_one