
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
