def f(x):
    return x ** 2 - 2 * x + 3


delta = 0.2
eps = 0.5
a0 = -2
b0 = 8
l = eps * 2

k = 0
CONST = (3 - 5 ** 0.5) / 2

print(f'k = {k}')

y = a0 + CONST * (b0 - a0)
print(f'y{k} = {y}')

z = a0 + b0 - y
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
        y = a0 + b0 - y
        print(f'y{k + 1} = {y}, z{k + 1} = {z}')
    else:
        a0 = y
        print(f'\n\n\nf(y{k}) > f(z{k}) =====> a{k+1} = y{k}, b{k+1} = b{k}')
        y = z
        z = a0 + b0 - z
        print(f'y{k + 1} = {y}, z{k + 1} = {z}')

    L = abs(a0 - b0)
    print(f'delta = {L}')

    if L <= l:
        print(f'\n\n\ndelta <= l =====> процесс поиска завершается')
        print(f'точка минимума принадлежит интервалу [{a0}, {b0}]')
        print(f'В качестве приближенного решения можно взять x* = {(a0 + b0) / 2}')
        break
    else:
        k += 1
        print(f'k = {k}')


