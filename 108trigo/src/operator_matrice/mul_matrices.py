##
## EPITECH PROJECT, 2020
## 108
## File description:
## mul_matrices.py
##

def get_result_line(matrice):
    result_line = []
    for x in range(len(matrice[0])):
        result_line.append(0)
    return result_line

def get_result_matrice(mat_one, mat_two):
    result_mat = []
    for x in range(len(mat_one)):
        result_mat.append(get_result_line(mat_two))
    return result_mat

def check_one_line(mat):
    tmp = []
    tmp.append(mat)
    try:
        len(tmp[0][0])
    except TypeError:
        return tmp
    return mat

def mul_mat(mat_one, mat_two):
    mat_one = check_one_line(mat_one)
    mat_two = check_one_line(mat_two)
    result = get_result_matrice(mat_one, mat_two)

    for x in range(len(mat_one)):
        for i in range(len(mat_two[0])):
            for n in range(len(mat_two)):
                result[x][i] += mat_one[x][n] * mat_two[n][i]
    return result
