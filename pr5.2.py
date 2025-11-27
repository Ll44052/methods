

# Исходная функция 0.785398
def f(x):
    return 1/(1+x**2)     


# Формула трапеций
def trapezoid(a, x, n=1000):
    
    if x == a:
        return 0.0

    h = (x - a) / n
    s = (f(a) + f(x)) / 2
    t = a

    for _ in range(1, n):
        t += h
        s += f(t)

    return s * h


# Поиск решения уравнения (бисекция)
def search_solution(a, b, left, right, eps=1e-6):
    
    while right - left > eps:
        mid = (left + right) / 2
        Fmid = trapezoid(a, mid)

        if Fmid < b:
            left = mid
        else:
            right = mid
    h = (left + right) / 2
    if abs(h - right) <= eps or abs(h - left) <= eps:
        print('Попробуйте увеличить интервал поиска решения')
    return h



a = float(input('Введите a: '))
b = float(input('Введите b: '))
         

left, right = list(map(float, input('Введите интервал поиска решения (от l до r): ').split()))

x_solution = search_solution(a, b, left, right)
print("Решение уравнения: ", round(x_solution, 4))
