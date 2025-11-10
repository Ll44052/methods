import matplotlib.pyplot as plt

# Функция для расчета разделеннх разностей
def f(x, y):
    if len(x) == 2 and len(y) == 2:
        return (y[1] - y[0]) / (x[1] - x[0])
    elif len(x) < 2 and len(y) < 2:
        return y[0]
    return (f(x[1:], y[1:]) - f(x[:-1], y[:-1])) / (x[-1] - x[0])

#Вспомогательная функция для расчета всех необходимых разделенных разностей для интерполирования назад
def dif(x, y):
    x1 = x[::-1]
    y1 = y[::-1]
    answer = []
    for i in range(1, len(x) + 1):
        answer.append(f(x1[:i], y1[:i]))
    return answer





#Функция ввода

# Интерполированиe назад
def L(x, y, difr, x0):
    x = x[::-1]
    y = y[::-1]
    a = 1
    answer = y[0]
    for i in range(len(x)):
        a *= (x0-x[i])
        answer += a * difr[i]
    return answer


x = [0, 1, 2]
x = x[::-1]
print(x[0:3])
x = []
y = []
y = [i**2 for i in x]
plt.figure()
plt.plot(x, y)
plt.show()