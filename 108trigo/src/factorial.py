##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## factoriel.py
##

def factorial(num):
    result = 1
    for x in range(1, num + 1):
        result *= x
    return result