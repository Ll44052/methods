import math
def proizv(x, f, i):
    try: 
        dX = 1e-10 
        x_new = x.copy() 
        x_new[i] += dX 
        return (f(x_new) - f(x)) / dX
    except Exception: 
        print(f'Ошибка: для уравнения не существует частной производной по x{i}') 
        exit()


def norm(x):
    try:
        return sum(i**2 for i in x) ** 0.5
    except Exception:
        print('Система плохо обусловлена')
        exit()


def seidel_newton(f, x0, e=1e-10, max_outer=50, max_inner=10, h=1e-8):

    x = x0.copy()
    n = len(x)

    for outer in range(max_outer):
        old_x = x.copy()

        for i in range(n):
            for _ in range(max_inner):
                fi = f[i](x)
                dfi = proizv(x, f[i], i)
                if abs(dfi) < 1e-12:
                    dfi = 1e-12

                delta = fi / dfi
                if delta > 1: delta = 1
                if delta < -1: delta = -1

                x[i] -= delta

                if abs(delta) < e:
                    break

        if norm([x[i] - old_x[i] for i in range(n)]) < e:
            print(f"Сошлась за {outer+1} итераций")
            return x

    print("Система не сошлась")
    return x



def f1(x): return x[0]**2 - 1        # x = 1
def f2(x): return x[1]**3 - 8        # y = 2
def f3(x): return x[2] - 3           # z = 3

x0 = [0.3, 1.0, 0.0]   

res = seidel_newton([f1, f2, f3], x0)
print("Решение:", res)
