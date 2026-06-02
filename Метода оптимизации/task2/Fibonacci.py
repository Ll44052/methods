def f(x):
    return x ** 2 - 2 * x + 3



delta = 0.2
eps = 0.5
a0 = -2
b0 = 8
l = eps * 2

def fib(x):
    k = 1
    x0 = 1
    x1 = 1
    answer = [x0, x1]
    while (x1 < x):
        a = x0 + x1
        x0 = x1
        x1 = a
        answer.append(x1)
        k += 1
    return k, answer


N, FN = fib(abs(b0 - a0) / l)
print(f'Количество вычислений N = {N}')
print(f'Числа Фибоначчи: {FN}')

k = 0
print(f'k = {k}')
y = a0 + (b0 - a0) * (FN[-3] / FN[-1])
z = a0 + (b0 - a0) * (FN[-2] / FN[-1])

print(f'y{k} = {y}')
print(f'z{k} = {z}')

while(True):
        
    fy = f(y)
    print(f'f(y{k}) = {fy}')

    fz = f(z)
    print(f'f(z{k}) = {fz}')

    if fy <= fz:
        b0 = z
        print(f'\n\n\nf(y{k}) <= f(z{k}) =====> a{k+1} = a{k}, b{k+1} = z{k}')
        z = y
        y = a0 + (b0 - a0) * (FN[-1-k-3] / FN[-1-k-1])
        print(f'y{k + 1} = {y}, z{k + 1} = {z}')
    else:
        a0 = y
        print(f'\n\n\nf(y{k}) > f(z{k}) =====> a{k+1} = y{k}, b{k+1} = b{k}')
        y = z
        z = a0 + (b0 - a0) * (FN[-1-k-2] / FN[-1-k-1])
        print(f'y{k + 1} = {y}, z{k + 1} = {z}')

    if k != N - 3:
        k += 1
        print(f'k = {k}')
    else:
        y = z
        z = y + delta
        if f(y) <= f(z):
            b0 = z
        else:
            a0 = y
        print(f'k = N - 3 =====> Завершаем процесс поиска')
        print(f'точка минимума принадлежит интервалу [{a0}, {b0}]')
        print(f'В качестве приближенного решения можно взять x* = {(a0 + b0) / 2}')
        break