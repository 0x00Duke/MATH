##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## get_div_mat.py
##

from src.operator_matrice.powered_matrices import powering_mat
from src.operator_matrice.div_matrice import div_matrice
from src.factorial import factorial

def get_div_mat(matrice, n):
    elevated_matrice = powering_mat(n, matrice, matrice)
    return div_matrice(factorial(n), elevated_matrice)