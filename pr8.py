import math
import matplotlib.pyplot as plt


# Система:
# y' = z
# z' = -y 
#0 1 1
def f1(x, y, z):
    return z


def f2(x, y, z):
    return -y


# Аналитическое решение
# y = sin(x) + cos(x)
# z = cos(x) - sin(x)

def decision_y(x):
    return math.sin(x) + math.cos(x)


def decision_z(x):
    return math.cos(x) - math.sin(x)


h = float(input('Введите h: '))
x0 = float(input('Введите x0: '))
y0, z0 = map(float, input('Введите y0 и z0: ').split())
b = float(input('Введите b: '))


x1 = x0
y1 = y0
z1 = z0

l_x = []
l_y = []
l_z = []


while x1 <= b:
    l_x.append(x1)
    l_y.append(y1)
    l_z.append(z1)

    y_new = y1 + h * f1(x1, y1, z1)
    z_new = z1 + h * f2(x1, y1, z1)

    y1 = y_new
    z1 = z_new
    x1 += h


an_y = []
an_z = []

for x in l_x:
    an_y.append(decision_y(x))
    an_z.append(decision_z(x))


delta_y = []
delta_z = []

with open('C:/Users/NND01/Desktop/числаки/data/output.txt', 'w') as f:
    f.write('Численное решение y:\n')
    f.write(' '.join(map(str, l_y)))

    f.write('\n\nАналитическое решение y:\n')
    f.write(' '.join(map(str, an_y)))

    f.write('\n\nDelta y:\n')
    for i in range(len(l_x)):
        d = an_y[i] - l_y[i]
        delta_y.append(d)
        f.write(str(d) + '\n')

    f.write(f'\nMax delta y = {max(delta_y)}')
    f.write(f'\nСреднее delta y = {sum(delta_y) / len(delta_y)}\n\n')

    f.write('Численное решение z:\n')
    f.write(' '.join(map(str, l_z)))

    f.write('\n\nАналитическое решение z:\n')
    f.write(' '.join(map(str, an_z)))

    f.write('\n\nDelta z:\n')
    for i in range(len(l_x)):
        d = an_z[i] - l_z[i]
        delta_z.append(d)
        f.write(str(d) + '\n')

    f.write(f'\nMax delta z = {max(delta_z)}')
    f.write(f'\nСреднее delta z = {sum(delta_z) / len(delta_z)}')


plt.plot(l_x, l_y, label='Численное y')
plt.plot(l_x, an_y, label='Аналитическое y')

plt.plot(l_x, l_z, label='Численное z')
plt.plot(l_x, an_z, label='Аналитическое z')

plt.legend()
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Метод Эйлера для системы ОДУ')
plt.show()