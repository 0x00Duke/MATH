##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## cos.py
##

from src.operator_matrice.add_matrices import add_matrices
from src.operator_matrice.sub_matrices import sub_matrices
from src.operator_matrice.powered_matrices import powering_mat
from src.factorial import factorial
from src.operator_matrice.div_matrice import div_matrice
from src.print_mat import print_matrice
from src.get.get_div_mat import get_div_mat
from src.get.get_basic_mat import basic_mat

def cos(matrice):
    result = basic_mat(matrice)

    for n in range(1, 50):
        next_mat = div_matrice(factorial(2 * n) , powering_mat(2 * n, matrice, matrice))
        if n % 2 != 0:
            result = sub_matrices(result, next_mat)
        else:
            result = add_matrices(result, next_mat)
    return result