# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())

all_a = sum((1 for l in combinations(letters, k) if 'a' in l))
print(all_a/len(list(combinations(letters, k))))
