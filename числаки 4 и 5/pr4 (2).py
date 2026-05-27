import matplotlib.pyplot as plt
import math



# Исходные данные задачи
a = 0
b = 1
n = 20

alpha1 = 1
alpha2 = 1

beta1 = 2
beta2 = 0



# Функции
def p(x):
    return x


def f(x):
    return math.sin(x)


# шаг сетки
h = (b - a) / n

# сетка
x = [a + i * h for i in range(n + 1)]


# Создание матрицы
A = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
B = [0 for _ in range(n + 1)]


# Левое граничное условие
# y'(a)-α1y(a)=α2
# (y1-y0)/h - α1y0 = α2
A[0][0] = -1 / h - alpha1
A[0][1] = 1 / h
B[0] = alpha2


# Внутренние точки
for i in range(1, n):
    A[i][i - 1] = 1 / h**2
    A[i][i] = -2 / h**2 - p(x[i])
    A[i][i + 1] = 1 / h**2
    B[i] = f(x[i])



# Правое граничное условие
# y'(b)-β1y(b)=β2
# (yn-yn-1)/h - β1yn = β2
A[n][n - 1] = -1 / h
A[n][n] = 1 / h - beta1
B[n] = beta2



# Метод Гаусса
def gauss(A, B):
    n = len(B)

    for i in range(n):
        pivot = A[i][i]

        for j in range(i, n):
            A[i][j] /= pivot
        B[i] /= pivot

        for k in range(i + 1, n):
            factor = A[k][i]

            for j in range(i, n):
                A[k][j] -= factor * A[i][j]

            B[k] -= factor * B[i]

    y = [0] * n

    for i in range(n - 1, -1, -1):
        y[i] = B[i]

        for j in range(i + 1, n):
            y[i] -= A[i][j] * y[j]

    return y


# решение
y = gauss(A, B)



# Вывод
print("Решение:")

for i in range(n + 1):
    print(f"x = {x[i]:.3f}, y = {y[i]:.6f}")



plt.plot(x, y, marker='o')
plt.title("Решение краевой задачи")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()