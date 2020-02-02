# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
words = {}

for i in range(n):
    inp = input()
    if inp in words.keys():
        words[inp] += 1
    else:
        words[inp] = 1

print(len(words))
[print(value, end=' ') for value in words.values()]
