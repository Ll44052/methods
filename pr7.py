import math
import  matplotlib.pyplot as plt


# (-2/(3*x**2)) - ((y**2)/3)   y(1) = 1.5
#(x/y)*math.exp(2*x) + y      y(0) = 1
def f(x, y):
    return math.exp(-math.sin(x)) - y*math.cos(x)


# 1/x + 1/(x**(2/3)+x)
#math.sqrt((x**2 + 1)*math.exp(2*x))
def decision(x):
    return (1 + x)*math.exp(-math.sin(x))

h = float(input('Введите h:'))
x0, y0 = map(float, input('Введите x0 и y0 (начальные условия y(x0) = y0):').split())
b = float(input('Введите b:'))

y1 = y0
x1 = x0
l_x = []
l_y = []

while x1 <= b:
    l_x.append(x1)
    l_y.append(y1)
    y1 += h*f(x1, y1)
    x1 += h

an_y = []
for i in l_x:
    an_y.append(decision(i))

delta = []
with open('C:/Users/NND01/Desktop/числаки/data/output.txt', 'w') as f:
    f.write(' '.join(map(str, l_y)))
    f.write('\n\n\n')
    f.write(' '.join(map(str, an_y)))
    f.write('\n\n\nDelta:\n')
    for i in range(len(l_x)):
        delta.append(an_y[i] - l_y[i])
        f.write(str(an_y[i] - l_y[i]) + '\n')
    f.write(f'Max delta = {max(delta)}, Среднее значение delta = {sum(delta) / len(delta)}')

plt.plot(l_x, l_y, label = 'Численное решение')
plt.plot(l_x, an_y, label = 'Аналитическое решение')
plt.legend()
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Метод Эйлера')
plt.show()
