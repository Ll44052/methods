import matplotlib.pyplot as plt


#Вспомогательная функция для расчета всех необходимых разделенных разностей для интерполирования назад
def dif(x, y):
    n = len(x)
    coef = y.copy()  
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def L(x1, y1, x):
    x_data = x1[::-1]
    y_data = y1[::-1]
    coef = dif(x_data, y_data)
    n = len(coef) - 1
    result = coef[n]
    
    for k in range(1, n + 1):
        result = coef[n - k] + (x - x_data[n - k]) * result
    return result

# Интерполированиe назад
""" def L(x, y, difr, x0):
    x = x[::-1]
    y = y[::-1]
    a = 1
    answer = y[0]
    for i in range(len(x)):
        a *= (x0-x[i])
        answer += a * difr[i]
    return answer
 """

#Функция ввода
def input(file):
    x = []
    y = []
    try:
        f = open(file, 'r')
        x = list(map(float, f.readline().split()))
        y = list(map(float, f.readline().split()))
    except Exception:
        print("Ошибка ввода")
        exit()
    f.close()
    if len(x) != len(y):
        print("Ошибка ввода")
        exit()
    return (x, y)



#Разбиение оси абсцисс
def splitX(x, s):
    answer = [x[0]]
    a = x[0]
    while a < x[-1]:
        a += s
        answer.append(a)
    return answer


file = 'C:/Users/NND01/Desktop/pr2/in.txt'
x, y = input(file)


answerX = splitX(x, 0.1)

answerY = []
for i in answerX:
    answerY.append(L(x, y, i))



plt.figure()
plt.plot(answerX, answerY, 'r')
plt.plot(x, y, 'g')
plt.legend([u'Результат', u'Исходные данные'])
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'Интерполирование назад')
plt.show()