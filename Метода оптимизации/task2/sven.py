def f(x):
    return x**2 - 2*x + 3


x0 = -2
delta = 0.2




f_left = f(x0 - delta)
f0 = f(x0)
f_right = f(x0 + delta)

print(f"f(x0-delta) = {f_left}")
print(f"f(x0)       = {f0}")
print(f"f(x0+delta) = {f_right}")


if f_left >= f0 >= f_right:
    direction = 1
    print("\nПоиск вправо")
elif f_left <= f0 <= f_right:
    direction = -1
    print("\nПоиск влево")
else:
    print("\nМинимум уже локализован")
    print(f"[{x0-delta}, {x0+delta}]")
    exit()

k = 0
x_prev = x0
x_curr = x0 + direction * delta

while True:

    x_next = x0 + direction * (2 ** (k + 1)) * delta

    f_curr = f(x_curr)
    f_next = f(x_next)

    print()
    print(f"k = {k}")
    print(f"x{k+1} = {x_curr}")
    print(f"f(x{k+1}) = {f_curr}")

    if f_next >= f_curr:

        if direction > 0:
            a = x_prev
            b = x_next
        else:
            a = x_next
            b = x_prev

        print("\nМинимум локализован")
        print(f"[{a}, {b}]")

        break

    x_prev = x_curr
    x_curr = x_next

    k += 1