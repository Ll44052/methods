n = int(input('Количество штатов: '))


states = {}
for i in range(n):
    states[f'Штат{i + 1}'] = int(input(f'Штат{i + 1} '))

print('Результаты голосования: ')


votes = {}  # {штат: {кандидат: голоса}}

while True:
    s = input()
    if s == "":
        break
    state, candidate = s.split()
    if state not in states:
        print("Такого штата нет")
        continue


    if state not in votes:
        votes[state] = {}

    if candidate not in votes[state]:
        votes[state][candidate] = 0

    votes[state][candidate] += 1
    



result = {}

for state in states.keys():
    candidates = votes[state]

    max_votes = max(candidates.values())

    winners = []
    for c in candidates.keys():
        if candidates[c] == max_votes:
            winners.append(c)

    winner = min(winners)

    if winner not in result:
        result[winner] = 0

    result[winner] += states[state]


sorted_res = sorted(result.items(), key=lambda x: (-x[1], x[0]))




for name, v in sorted_res:
    print(name, v)



