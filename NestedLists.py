if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

minimum = min(scores)
while min(scores) == minimum:
    names.pop(scores.index(min(scores)))
    scores.pop(scores.index(min(scores)))

min_names = []
for i in range(len(scores)):
    if scores[i] == min(scores):
        min_names.append(names[i])
for i in range(len(min_names)):
    print(min(min_names))
    min_names.remove(min(min_names))



'''#Next solution'''

if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)

minimum = min(scores)
while min(scores) == minimum:
    names.pop(scores.index(min(scores)))
    scores.pop(scores.index(min(scores)))

min_names = []
for i in range(len(scores)):
    if scores[i] == min(scores):
        min_names.append(names[i])
for i in range(len(min_names)):
    print(min(min_names))
    min_names.remove(min(min_names))
