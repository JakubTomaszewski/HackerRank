# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
n = input().split()
perms = sorted(permutations(n[0], int(n[1])))
for per in perms:
    print(''.join(p for p in per))
    

