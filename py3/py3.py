

with open('C:/Users/NND01/Desktop/pr2/file.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    capacity = list(map(int, f.readline().split()))
    tasks = list(map(int, f.readline().split()))

if n != len(capacity) or m != len(tasks):
    print('Ошибка ввода')
    exit()


used = [0] * n
assign = [[] for _ in range(n)]


for t in tasks:
    best = 0
    for i in range(1, n):
        if used[i] / capacity[i] < used[best] / capacity[best]:
            best = i

    used[best] += t
    assign[best].append(t)


# вывод
loads = []
out = open('C:/Users/NND01/Desktop/pr2/out.txt', 'w')

for i in range(n):
    percent = used[i] / capacity[i] * 100
    loads.append(percent)

    print(f"Узел {i+1} ({capacity[i]}):", end=" ", file=out)
    print(assign[i], end=" ", file=out)
    print(f"- загрузка: {used[i]}/{capacity[i]} = {percent:.1f}%", file=out)

# среднее
avg = sum(loads) / n
print(f"\nСредняя загрузка: {avg:.1f}%", file=out)

# отклонения
devs = []
for p in loads:
    d = abs(p - avg)
    devs.append(d)

print("Отклонения:", end=" ", file=out)
for d in devs:
    print(f"{d:.1f}", end=" ", file=out)

# среднее отклонение
avg_dev = sum(devs) / n
print(f"\nСреднее отклонение: {avg_dev:.2f}%", file=out)
