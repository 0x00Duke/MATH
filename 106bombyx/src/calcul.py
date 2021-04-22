##
## EPITECH PROJECT, 2020
## B-MAT-200-BAR-2-1-106bombyx-jose-antonio.rodriguez-assalone
## File description:
## calcul.py
##

from sys import argv as av

def simple_calcul():
    n = int(av[1])
    k = float(av[2])
    x = 2

    print("1 %.2f" % n)
    while x <= 100:
        n = (k * n) * ((1000 - n) / 1000)
        if n <= 0 :
            print("%d 0.00" % x)
        else :
            print("%d %.2f" % (x, n))
        x += 1

def complex_calcul():
    i = 1
    k = 1
    n = int(av[1])
    i0 = int(av[2])
    i1 = int(av[3])
    tmp = n

    while k <= 4:
        n = tmp
        while i < i0:
            n = (k * n) * ((1000 - n) / 1000)
            i += 1
        while i < i1 + 1:
            if (n <= 0):
                print("%.2f 0.00" % k)
            else :
                print("%.2f %.2f" % (k, n))
            n = (k * n) * ((1000 - n) / 1000)
            i += 1
        i = 1
        k += 0.01