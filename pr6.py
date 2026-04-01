# def inp(file):
#     matrix = []
#     try:
#         f = open(file, 'r')
#         a = f.readline()
#         while a != '':
#             matrix.append(list(map(float, a.split())))
#             a = f.readline()

#     except Exception:
#         print("Ошибка ввода")
#         exit()
#     f.close()
    
#     return matrix


# def vector_p(x, x1):
#     answer = 0
#     for i in range(len(x)):
#         answer += x[i] * x1[i]
#     return answer


# def matrix_p(matrix, x):
#     x_1 = []
#     for i in range(len(matrix)):
#         a = 0
#         for j in range(len(matrix)):
#             a += matrix[i][j] * x[j]
#         x_1.append(a)
#     return x_1

# def normir(x, y):
#     answer = []
#     for i in range(len(x)):
#         answer.append(x[i] / y)
#     return answer

# # def norm(x, x_1):
# #     answer = []
# #     for i in range(len(x)):
# #         answer.append(abs(x[i] - x_1[i]))
# #     return max(answer)

# # def sob(x, y):
# #     l = []
# #     for i in range(len(x)):
# #         l.append(y[i] / x[i])
# #     return l

# matrix = inp('/home/dnn/числаки/data/matrix.txt')
# e = float(input('Введите погрешность: '))
# y0 = list(map(float, input('Введите начальное приближение: ').split()))
# l0 = 0


# s0 = vector_p(y0, y0)
# x0 = normir(y0, s0 ** 0.5)




# y1 = matrix_p(matrix, x0)
# s1 = vector_p(y1, y1)
# t1 = vector_p(y1, x0)
# x1 = normir(y1, s1 ** 0.5)

# l1 = s1 / t1

# iteration = 0

# while abs(l1 - l0) > e:
#     x0 = x1
#     l0 = l1

#     y1 = matrix_p(matrix, x0)
#     s1 = vector_p(y1, y1)
#     t1 = vector_p(y1, x0)
#     x1 = normir(y1, s1 ** 0.5)
#     l1 = s1 / t1
#     iteration += 1
# print(l1, x1)
# print(iteration)






def inp(file):
    matrix = []
    try:
        with open(file, 'r') as f:
            for line in f:
                matrix.append(list(map(float, line.split())))
    except Exception:
        print("Ошибка ввода")
        exit()
    return matrix


def vector_p(x, x1):
    return sum([x[i] * x1[i] for i in range(len(x))])


def matrix_p(matrix, x):
    return [
        sum(matrix[i][j] * x[j] for j in range(len(x)))
        for i in range(len(matrix))
    ]


def normir(x, norm):
    return [xi / norm for xi in x]


# процесс Эйткена
def aitken(l0, l1, l2):
    denom = l2 - 2*l1 + l0
    if abs(denom) < 1e-14:
        return l2  
    return l0 - (l1 - l0)**2 / denom



matrix = inp('/home/dnn/числаки/data/matrix.txt')

e = float(input('Введите погрешность: '))
y0 = list(map(float, input('Введите начальное приближение: ').split()))

# нормировка начального вектора
s0 = vector_p(y0, y0)
x0 = normir(y0, s0**0.5)

# первые две итерации
y1 = matrix_p(matrix, x0)
s1 = vector_p(y1, y1)
t1 = vector_p(y1, x0)
x1 = normir(y1, s1**0.5)

l0 = s1 / t1


y2 = matrix_p(matrix, x1)
s2 = vector_p(y2, y2)
t2 = vector_p(y2, x1)
x2 = normir(y2, s2**0.5)

l1 = s2 / t2

# Эйткен
l_acc = aitken(l0, l1, l1)

iteration = 0

while True:

    y3 = matrix_p(matrix, x2)
    s3 = vector_p(y3, y3)
    t3 = vector_p(y3, x2)
    x3 = normir(y3, s3**0.5)

    l2 = s3 / t3

    # ускоренное значение
    l_acc_new = aitken(l0, l1, l2)


    if abs(l_acc_new - l_acc) < e:
        break

    # сдвиг
    l0, l1 = l1, l2
    x2 = x3
    l_acc = l_acc_new

    iteration += 1


print("\nСобственное значение:", l_acc_new)
print("Собственный вектор:", x3)
print("Количество итераций:", iteration)