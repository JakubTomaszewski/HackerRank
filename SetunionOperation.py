# Enter your code here. Read input from STDIN. Print output to STDOUT

en_n = int(input())
en = set(input().split())

fr_n = int(input())
fr = set(input().split())

print(len(en.union(fr)))



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

en_n = int(input())
en = set(input().split())

fr_n = int(input())
fr = set(input().split())

print(len(en)+len(fr)-len(en.intersection(fr)))
