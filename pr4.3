import math

def proizv_scalar(f, x, i):
    
    dX = 1e-8
    x1 = x.copy()
    x2 = x.copy()
    x1[i] += dX
    x2[i] -= dX
    return (f(x1) - f(x2)) / (2 * dX)


def norm(x):
    return sum(i**2 for i in x) ** 0.5


def seidel_newton(f, x0, e=1e-10, max_outer=50, max_inner=10):

    x = x0.copy()
    n = len(x)

    for outer in range(max_outer):
        old_x = x.copy()

        for i in range(n):
            for _ in range(max_inner):

                fi = f[i](x)
                dfi = proizv_scalar(f[i], x, i)

                if abs(dfi) < 1e-12:
                    dfi = 1e-12

                delta = fi / dfi

                
                if delta > 1: delta = 1
                if delta < -1: delta = -1

                x[i] -= delta

                if abs(delta) < e:
                    break

        if norm([x[i] - old_x[i] for i in range(n)]) < e:
            print(f"Сошлась за {outer + 1} итераций")
            return x

    print("Система не сошлась")
    return x


# система
def f1(x): return x[0]**2 + x[1]**2 - 4 # x=-1.816264 y=0.837368
def f2(x): return math.exp(x[0]) + x[1] - 1

x0 = [1.0, -1.0]

res = seidel_newton([f1, f2], x0)

print('Решение:', *[round(i, 6) for i in res])
