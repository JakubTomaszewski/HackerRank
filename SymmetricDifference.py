# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

x = M.union(N)
for i in M.intersection(N):
    x.discard(i)

[print(e) for e in sorted(x)]




'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

x = M.union(N)
[x.discard(i) for i in M.intersection(N)]

[print(e) for e in sorted(x)]




'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
M = set(map(int, input().split()))
n = int(input())
N = set(map(int, input().split()))

x = M.union(N)
[x.discard(i) for i in M.intersection(N)]
[print(e) for e in sorted(x)]

