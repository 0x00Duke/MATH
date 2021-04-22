##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-108trigo-leon.ducasse
## File description:
## init_class.py
##

from src.math_fonctions.cos import cos
from src.math_fonctions.cosh import cosh
from src.math_fonctions.sin import sin
from src.math_fonctions.sinh import sinh
from src.math_fonctions.exp import exp

class math_fonction:
    def __init__(self, name, fonction):
        self.name = name
        self.fonction = fonction
    def returning(self, matrice):
        return self.fonction(matrice)

def init_classes():
    array = []
    array.append(math_fonction("COS", cos))
    array.append(math_fonction("COSH", cosh))
    array.append(math_fonction("SIN", sin))
    array.append(math_fonction("SINH", sinh))
    array.append(math_fonction("EXP", exp))
    return array
