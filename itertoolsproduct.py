# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = input().split()
B = input().split()
A = list(map(int, A))
B = list(map(int, B))

AxB = product(A, B)
for element in AxB:
    print(element, end=' ')





'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = input().split()
B = input().split()
A = list(map(int, A))
B = list(map(int, B))

AxB = product(A, B)
for element in AxB:
    print(element, end=' ')





'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))
