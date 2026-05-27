import matplotlib.pyplot as plt
import math


# ------------------------
# Параметры задачи
# ------------------------
alpha = 1
L = 1
T = 0.1

nx = 20
nt = 200

h = L / nx
tau = T / nt

r = alpha * tau / (h * h)

print("r =", r)

if r > 0.5:
    print("Схема неустойчива!")
    exit()


# ------------------------
# Сетка
# ------------------------
x = [i * h for i in range(nx + 1)]


# ------------------------
# Начальное условие
# U(0,x)=sin(pi*x)
# ------------------------
U = [[0 for _ in range(nx + 1)] for _ in range(nt + 1)]

for i in range(nx + 1):
    U[0][i] = math.sin(math.pi * x[i])


# ------------------------
# Явная схема
# ------------------------
for n in range(nt):

    # внутренние точки
    for i in range(1, nx):
        U[n + 1][i] = U[n][i] + r * (
            U[n][i + 1]
            - 2 * U[n][i]
            + U[n][i - 1]
        )

    # граничные условия Фон Неймана O(h)
    U[n + 1][0] = U[n + 1][1]
    U[n + 1][nx] = U[n + 1][nx - 1]



# Построение графика

plt.figure(figsize=(10, 6))

times = [0, nt//4, nt//2, 3*nt//4, nt]

for n in times:
    plt.plot(x, U[n], label=f"t={n*tau:.3f}")

plt.title("Уравнение теплопроводности")
plt.xlabel("x")
plt.ylabel("U(t,x)")
plt.grid(True)
plt.legend()
plt.show()