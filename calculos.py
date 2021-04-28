import matplotlib.pyplot as pl
import math


def portadoraPM(Vp, fp, time):
    return Vp * math.cos(2 * math.pi * fp * time)


def moduladoraPM(Vm, fm, time):
    return Vm * math.sin(2 * math.pi * fm * time)


def moduladaPM(Vp, t, m, fm):
    return Vp * math.cos(2 * math.pi * t + m * math.sin(2 * math.pi * fm * t))


def portadoraFM(Vp, fp, t):
    return Vp * math.sin(2 * math.pi * fp * t)


def moduladoraFM(Vm, fm, t):
    return Vm * math.sin(2 * math.pi * fm * t)


def moduladaFM(Vp, fp, t, fm, f):
    m = f / fm
    return Vp * math.sin(2 * math.pi * fp * t + m * math.cos(2 * math.pi * fm * t))


def deltaV(Vm, k1):
    v = Vm * k1
    return v


def sensibilidadK(Vm, f, fm):
    m = f / fm
    K = m / Vm
    return K


def sensibilidadK2(Vm, m):
    K = m / Vm
    return K


def deltaf(m, fm):
    v = m * fm
    return v


def npares(m):
    if m == 0.0:
        return 0
    elif m == 0.25:
        return 1
    elif m == 0.5:
        return 2
    elif m == 1.0:
        return 3
    elif m == 1.5:
        return 4
    elif m == 2.0:
        return 4
    elif m == 2.5:
        return 5
    elif m == 3.0:
        return 6
    elif m == 4.0:
        return 7
    elif m == 5.0:
        return 8
    elif m == 6.0:
        return 9
    elif m == 7.0:
        return 10
    elif m == 8.0:
        return 11
    else:
        return False
