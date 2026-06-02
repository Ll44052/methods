import numpy as np
def f(x):
    x1, x2 = x
    return x1 ** 2 + 4 * x2 ** 2 - x1 * x2 + x1

def grad(x, h = 1e-5):
    x1, x2 = x
    g1 = (f([x1 + h, x2]) - f([x1, x2])) / h
    g2 = (f([x1, x2 + h]) - f([x1, x2])) / h
    return np.array([g1, g2])


def hessian(x, h=1e-4):
    n = len(x)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                xp = np.array(x, dtype=float)
                xm = np.array(x, dtype=float)
                xp[i] += h
                xm[i] -= h
                H[i, i] = (
                    f(xp)
                    - 2*f(x)
                    + f(xm)
                ) / h**2
            else:
                xpp = np.array(x, dtype=float)
                xpm = np.array(x, dtype=float)
                xmp = np.array(x, dtype=float)
                xmm = np.array(x, dtype=float)

                xpp[i] += h
                xpp[j] += h

                xpm[i] += h
                xpm[j] -= h

                xmp[i] -= h
                xmp[j] += h

                xmm[i] -= h
                xmm[j] -= h

                H[i, j] = (
                    f(xpp)
                    - f(xpm)
                    - f(xmp)
                    + f(xmm)
                ) / (4*h*h)

    return H

x = np.array([3.0, 1.0])

eps1 = 1e-4
M = 100
k = 0
u = 1
while True:
    print(f'k = {k}')
    print(f'u{k} = {u}')

    g = grad(x)
    print(f'Градиент в точке {x} = {g}')

    if np.linalg.norm(g) < eps1:
        print(f'Норма градиента в точке {x} < {eps1} ======> x* = {x}')
        break

    if k >= M:
        print(f'k >= {M} ======> x* = {x}')
        break

    H = hessian(x)

    print(f"\nМатрица Гессе H(x{k}):")
    print(H)

    while True:
        H_mod = H + u * np.eye(2)
        print(f"\nМатрица H(x{k}) + u{k}*E:")
        print(H_mod)

        H_inv = np.linalg.inv(H_mod)

        print(f"\n(H(x{k}) + u{k}*E)^-1(x{k}):")
        print(H_inv)

        d = -H_inv @ g
        print(f'd{k} = {d}')

        x_new = x + d
        print(f'x{k+1} = {x_new}')

        if f(x_new) < f(x):
            k += 1
            u /= 2
            x = x_new
            print(f'f(x{k}) < f(x{k-1}) ======> k = {k}, u = {u}')
            break
        else:
            print(f'f(x{k + 1}) >= f(x{k}) ======> u = {2*u}')
            u *= 2