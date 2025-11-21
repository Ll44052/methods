import math



#Частная производная функции
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
        print('Система не стабильна')
        exit()


def method(f, x_0, e=1e-10, max_iter=100):

    x = x_0.copy()
    n = 0
    for k in range(max_iter):
        old_x = x.copy()
        for i in range(len(f)):
            fi = f[i](x)
            dfi = proizv(x, f[i], i)
            if abs(dfi) < 1e-12:
                dfi = 1e-12
            x[i] -= fi / dfi
        n = norm([old_x[i] - x[i] for i in range(len(old_x))])
        if n < e:
            print(f"Система сошлась за {k + 1} операции")
            break
        
    return x


x_0 = [1, 1, 1] #Начальное приближение

# Система (овет x0: pi/2, x1: 0)
def f1(x): return x[0]**2 - 1        # x = 1
def f2(x): return x[1]**3 - 8        # y = 2
def f3(x): return x[2] - 3           # z = 3

result = method([f1, f2, f3], x_0, e = 1e-8, max_iter=100)

for i in range(len(result)):
    print(f'x{i} = {round(result[i])}')


