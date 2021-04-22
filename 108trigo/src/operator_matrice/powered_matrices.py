##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## powered_matrices.py
##

from src.operator_matrice.mul_matrices import mul_mat

def powering_mat(power, first_matrice, matrice):
    if power > 1:
        matrice = mul_mat(matrice, first_matrice)
        power -= 1
        return powering_mat(power, first_matrice, matrice)
    return matrice