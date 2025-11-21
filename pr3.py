import math

# x**3 + 2x**2 - 1 (ответ: -1.618, -1, 0.618)
# x**3 + 2x

#Исходная функция
def f(x):
    return math.cos(x) - 1

#Разбиение оси абсцисс
def splitX(a, b, s):
    answer = []
    x = a
    while x <= b:
        answer.append(x)
        x = round(x + s, 10) 
    return answer



#Производная исходной функции
def proizv(x):
    dX = 1e-10
    return (f(x + dX) - f(x)) / dX

# Метод Ньютона
def methodN(x):
    if proizv(x) == 0:
        return x
    return x - (f(x) / proizv(x))

#Находим интервалы с корнями
def findInterval(a, b, s=0.1):
    v = splitX(a, b, s)
    eps = 1e-4
    intervals = []
    for i in range(1, len(v)):
        f1 = f(v[i-1])
        f2 = f(v[i])
        if abs(f1) < eps:
            intervals.append((v[i-1], v[i-1]))
        elif abs(f2) < eps:
            intervals.append((v[i], v[i]))
        elif f1 * f2 < 0:
            intervals.append((v[i-1], v[i]))
    return intervals



# Процесс Эйткена
def processAitken(x0, x1, x2):
    return ((x0*x2) - (x1**2)) / (x2 - 2 * x1 + x0)


def merge(a, eps=1e-2):
    a = sorted(a)
    merged = []
    current = a[0]

    for r in a[1:]:
        if abs(r - current) < eps:
            continue  # слишком близко, считаем тем же корнем
        merged.append(current)
        current = r

    merged.append(current)
    return merged



x = list(map(float, input('Введите [a, b]: ').split()))
e = float(input('Введите абсолютную допустимую погрешность: '))
s = float(input('Введите длину интервала для разбиения [a, b]: '))




interval = findInterval(x[0], x[1], s)
answer = set()
for a, b in interval:
    x0 = (a + b) / 2
    x1 = methodN(x0)
    x2 = methodN(x1)
    while True:
        if abs(f(x1)) < e:  # Проверяем, если значение функции близко к 0
            answer.add(round(x1, 4))
            break
        xa = processAitken(x0, x1, x2)
        x3 = methodN(xa)
        if abs(x3 - xa) < e:
            x0 = xa
            x1 = x3
            x2 = methodN(x1)
        else:
            answer.add(round(x3, 4))
            break


answer = merge(list(answer))


print('Корни уравнения: ')
for i in answer:
    print(i, end='; ')





