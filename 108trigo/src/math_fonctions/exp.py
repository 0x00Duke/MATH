##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## exp.py
##

from src.operator_matrice.add_matrices import add_matrices
from src.operator_matrice.powered_matrices import powering_mat
from src.operator_matrice.div_matrice import div_matrice
from src.print_mat import print_matrice
from src.get.get_div_mat import get_div_mat
from src.get.get_basic_mat import basic_mat
from copy import deepcopy

def exp(matrice):
    original_mat = deepcopy(matrice)
    matrice = add_matrices(matrice, basic_mat(matrice))

    for n in range(2, 100):
        matrice = add_matrices(matrice, get_div_mat(original_mat, n))
    return matrice