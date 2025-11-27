



# Исходная функция 0.785398
def f(x):
    return x**2+1

# n = n - 1
def trapezoid(a, b, h=0.01):
    exp = h
    if abs(b) <= exp:
        return a
    b = b*(2/h) - f(a)
    answer = a + h * 2
    while abs(f(answer) - b) > exp:
        b -= 2*f(answer - h)
        answer += h
    return answer



a = float(input('Введите a: '))
b = float(input('Введите b: '))

print('Ответ: ', round(trapezoid(a, b), 2))
