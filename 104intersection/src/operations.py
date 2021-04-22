
import math


def discriminant(a, b, c):

    determinant = b**2 - 4 * a * c
    return determinant


def num_solutions(determinant):

    if determinant == 0:
        return 1
    if determinant > 0:
        return 2
    if determinant < 0:
        return 0


def result_equation(a, b, c):

    if a == 0:
        print("No intersection point.")
        return 0
    disc = discriminant(a, b, c)
    num_sol = num_solutions(disc)
    if num_sol == 0:
        print("No intersection point.")
        return 0
    if num_sol == 1:
        print("1 intersection point:")
        return 1, -b / (2 * a)
    if num_sol == 2:
        print("2 intersection points:")
        sol1 = (-b + math.sqrt(disc)) / (2 * a)
        sol2 = (-b - math.sqrt(disc)) / (2 * a)
        return 2, sol1, sol2
    return 84


def coord_point(point, vector, t):

    result = [[], [], []]
    result[0] = point[0] + (t * vector[0])
    result[1] = point[1] + (t * vector[1])
    result[2] = point[2] + (t * vector[2])

