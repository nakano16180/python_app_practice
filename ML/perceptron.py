import numpy as np

# AND
def AND(x1, x2):
    x1_x2 = np.array(([x1, x2]))
    w0 = -0.8
    w1_w2 = np.array((0.5, 0.5))

    val = w0 + np.sum(x1_x2 * w1_w2)

    if val <= 0:
        return 0
    elif 0 < val:
        return 1


# NAND
def NAND(x1, x2):
    x1_x2 = np.array(([x1, x2]))
    w0 = 0.8
    w1_w2 = np.array((-0.5, -0.5))

    val = w0 + np.sum(x1_x2 * w1_w2)

    if val <= 0:
        return 0
    elif 0 < val:
        return 1


# OR
def OR(x1, x2):
    x1_x2 = np.array(([x1, x2]))
    w0 = -0.4
    w1_w2 = np.array((0.5, 0.5))

    val = w0 + np.sum(x1_x2 * w1_w2)

    if val <= 0:
        return 0
    elif 0 < val:
        return 1

# XOR
def XOR(x1, x2):
    _nand = NAND(x1, x2)
    _or = OR(x1, x2)

    _xor = AND(_nand, _or)
    return _xor