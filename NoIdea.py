# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many_nm = list(map(int, input().split()))

n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for i in range(how_many_nm[1]):
    if A[i] in n:
        happiness += 1
    if B[i] in n:
        happiness -= 1
print(happiness)



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many_nm = list(map(int, input().split()))

n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for i in range(how_many_nm[1]):
    if A[i] in n:
        happiness += 1
    if B[i] in n:
        happiness -= 1
print(happiness)



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many_nm = list(map(int, input().split()))

n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for i in range(how_many_nm[1]):
    if A[i] in n:
        happiness += 1
    else:
        continue
    if B[i] in n:
        happiness -= 1
    else:
        continue
print(happiness)



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

how_many_nm = list(map(int, input().split()))

n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for i in range(how_many_nm[1]):
    if A[i] in n:
        happiness += 1
    if B[i] in n:
        happiness -= 1
print(happiness)



'''#Next solution'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many_nm = list(map(int, input().split()))

n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for element in n:
    if element in A:
        happiness += 1
    if element in B:
        happiness -= 1
print(happiness)



'''#Next solution'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many_nm = list(map(int, input().split()))

n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for element in n:
    if element in A and not(element in B):
        happiness += 1
    elif element in B:
        happiness -= 1
print(happiness)



'''#Next solution'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many_nm = list(map(int, input().split()))

n = iter(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
happiness = 0
for element in n:
    if element in A and not(element in B):
        happiness += 1
    elif element in B:
        happiness -= 1
print(happiness)



'''#Next solution'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many = list(map(int, input().split()))

n = input().split()
A = input().split()
B = input().split()


happiness = sum([((n[i] in A) - (n[i] in B)) for i in range(how_many[0])])
print(happiness)



'''#Next solution'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
how_many = list(map(int, input().split()))

n = input().split()
A = input().split()
B = input().split()


happiness = sum( ((n[i] in A) - (n[i] in B)) for i in range(how_many[0]) )
print(happiness)



'''#Next solution'''


# Enter your code here. Read input from STDIN. Print output to STDOUT



from collections import Counter

n_and_m = input() # i don't use n or m

nums = Counter(input().split(' '))

get_nums = lambda inp: [n for n in inp.split(' ')]
pos = get_nums(input())
neg = get_nums(input())

happiness = sum(
    [nums.get(num, 0) for num in pos]
    + [-nums.get(num, 0) for num in neg]
    )

print(happiness)



'''#Next solution'''


# Enter your code here. Read input from STDIN. Print output to STDOUT



from collections import Counter

n_and_m = input()

nums = Counter(input().split(' '))

get_nums = lambda inp: [n for n in inp.split(' ')]
pos = get_nums(input())
neg = get_nums(input())

happiness = sum(
    [nums.get(num, 0) for num in pos]
    + [-nums.get(num, 0) for num in neg]
    )

print(happiness)
