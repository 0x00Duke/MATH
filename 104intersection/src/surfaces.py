
from .operations import discriminant, num_solutions, result_equation, coord_point
import math


def sphere(av):

    xp = int(av[2])
    yp = int(av[3])
    zp = int(av[4])
    xv = int(av[5])
    yv = int(av[6])
    zv = int(av[7])

    a = (xv**2 + yv**2 + zv**2)
    b = 2 * ((xp * xv) + (yp * yv) + (zp * zv))
    c = (xp**2 + yp**2 + zp**2) - int(av[8])**2
    t = result_equation(a, b, c)
    if t == 84:
        return 84
    if t == 0:
        return 0
    if t[0] == 1:
        coord = [xp + (t[1] * xv), yp + (t[1] * yv), zp + (t[1] * zv)]
        print("(%.3f, %.3f, %.3f)" % (coord[0], coord[1], coord[2]))
        return 0
    if t[0] == 2:
        coord1 = [xp + (t[1] * xv), yp + (t[1] * yv), zp + (t[1] * zv)]
        coord2 = [xp + (t[2] * xv), yp + (t[2] * yv), zp + (t[2] * zv)]
        print("(%.3f, %.3f, %.3f)" % (coord1[0], coord1[1], coord1[2]))
        print("(%.3f, %.3f, %.3f)" % (coord2[0], coord2[1], coord2[2]))
        return 0
    return 0


def cone(av):

    xp = int(av[2])
    yp = int(av[3])
    zp = int(av[4])
    xv = int(av[5])
    yv = int(av[6])
    zv = int(av[7])
    p = int(av[8])

    while not 0 < p < 90:
        if p == 0 or p == 90:
            return 84
        elif p > 90:
            p -= 90
        if p < 0:
            p += 90
    a = (xv**2 + yv**2 - (math.tan(math.radians(p)))**2 * (zv**2))
    b = (2 * (xp * xv + yp * yv - (math.tan(math.radians(p))**2 * zp * zv)))
    c = (xp**2 + yp**2 - (math.tan(math.radians(p)))**2 * (zp**2))
    t = result_equation(a, b, c)
    if t == 84:
        return 84
    if t == 0:
        return 0
    if t[0] == 1:
        coord = [xp + (t[1] * xv), yp + (t[1] * yv), zp + (t[1] * zv)]
        print("(%.3f, %.3f, %.3f)" % (coord[0], coord[1], coord[2]))
        return 0
    if t[0] == 2:
        coord1 = [xp + (t[1] * xv), yp + (t[1] * yv), zp + (t[1] * zv)]
        coord2 = [xp + (t[2] * xv), yp + (t[2] * yv), zp + (t[2] * zv)]
        print("(%.3f, %.3f, %.3f)" % (coord1[0], coord1[1], coord1[2]))
        print("(%.3f, %.3f, %.3f)" % (coord2[0], coord2[1], coord2[2]))
        return 0
    return 0


def cylinder(av):

    xp = int(av[2])
    yp = int(av[3])
    zp = int(av[4])
    xv = int(av[5])
    yv = int(av[6])
    zv = int(av[7])
    p = int(av[8])

    a = (xv**2 + yv**2)
    b = 2 * ((xp * xv) + (yp * yv))
    c = (xp**2 + yp**2) - p**2
    if a == 0 and b == 0 and c == 0:
        print("There is an infinite number of intersection points.")
        return 0
    t = result_equation(a, b, c)
    if t == 84:
        return 84
    if t == 0:
        return 0
    if t[0] == 1:
        coord = [xp + (t[1] * xv), yp + (t[1] * yv), zp + (t[1] * zv)]
        print("(%.3f, %.3f, %.3f)" % (coord[0], coord[1], coord[2]))
        return 0
    if t[0] == 2:
        coord1 = [xp + (t[1] * xv), yp + (t[1] * yv), zp + (t[1] * zv)]
        coord2 = [xp + (t[2] * xv), yp + (t[2] * yv), zp + (t[2] * zv)]
        print("(%.3f, %.3f, %.3f)" % (coord1[0], coord1[1], coord1[2]))
        print("(%.3f, %.3f, %.3f)" % (coord2[0], coord2[1], coord2[2]))
        return 0
    return 0

