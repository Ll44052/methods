import numpy as np
def f(x):
    x1, x2 = x
    return x1 ** 2 + 4 * x2 ** 2 - x1 * x2 + x1

def grad(x, h = 1e-5):
    x1, x2 = x
    g1 = (f([x1 + h, x2]) - f([x1, x2])) / h
    g2 = (f([x1, x2 + h]) - f([x1, x2])) / h
    return np.array([g1, g2])

def golden_section(phi, a=0.0, b=1.0, eps=1e-5):

    CONST = (3 - 5 ** 0.5) / 2

    y = a + CONST * (b - a)
    z = a + b - y

    while abs(b - a) > 2 * eps:

        if phi(y) <= phi(z):
            b = z
            z = y
            y = a + CONST * (b - a)

        else:
            a = y
            y = z
            z = a + b - z

    return (a + b) / 2

x = np.array([3.0, 1.0])

eps1 = 1e-4
eps2 = 1e-4

M = 100

k = 0
while True:
    print(f'k = {k}')
    g = grad(x)
    print(f'Градиент в точке {x} = {g}')

    if np.linalg.norm(g) < eps1:
        print(f'Норма градиента в точке {x} < {eps1} ======> x* = {x}')
        break

    if k >= M:
        print(f'k >= {M} ======> x* = {x}')
        break

    if k >= 1:
        b = (np.linalg.norm(g)**2) / (np.linalg.norm(grad(x_old)) ** 2)
        print(f'b{k-1} = {b}')
        d = -g + b * d
        print(f'd{k} = {d}')
    else:
        d = -g
        print(f'd{k} = {d}')
    
    phi = lambda t: f(x + t * d)
    t = golden_section(phi)
    print(f"t*{k} = {t}")

    x_new = x + t*d
    print(f'x{k+1} = {x_new}')

    if np.linalg.norm(x_new - x) < eps2 and abs(f(x_new) - f(x)) < eps2:
        print('Условия выполнены, поиск завершен.')
        print(f'x* = {x_new}')
        break
    else:
        k += 1
        x_old = x
        x = x_new
        