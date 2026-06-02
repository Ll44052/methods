def f(x):
    return x ** 2 - 2 * x + 3



delta = 0.2
eps = 0.5
a0 = -2
b0 = 8
l = eps * 2

k = 0

while(True):
    print(f'k = {k}')

    y = (a0 + b0 - delta) / 2
    print(f'y{k} = {y}')

    fy = f(y)
    print(f'f(y{k}) = {fy}')

    z = (a0 + b0 + delta) / 2
    print(f'z{k} = {z}')

    fz = f(z)
    print(f'f(z{k}) = {fz}')


    if fy <= fz:
        b0 = z
        print(f'\n\n\nf(y{k}) <= f(z{k}) =====> a{k+1} = a{k}, b{k+1} = z{k}')
    else:
        a0 = y
        print(f'\n\n\nf(y{k}) > f(z{k}) =====> a{k+1} = y{k}, b{k+1} = b{k}')

    L = abs(b0 - a0)
    print(f'|L{2*(k+1)}| = {L}')

    if L <= l:
        print(f'\n\n\n|L{2*(k+1)}| <= l =====> процесс поиска завершается')
        print(f'точка минимума принадлежит интервалу [{a0}, {b0}]')
        print(f'В качестве приближенного решения можно взять x* = {(a0 + b0) / 2}')
        break
    else:
        k += 1


