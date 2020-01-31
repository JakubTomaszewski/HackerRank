n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    else:
        eval('s.'+cmd[0]+'('+str(cmd[1])+')')
print(sum(s))






'''#Next solution'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] != 'pop':
        eval('s.{}({})'.format(cmd[0], cmd[1]))
    else: s.pop()
print(sum(s))






'''#Next solution'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    else:
        eval('s.'+cmd[0]+'('+str(cmd[1])+')')
print(sum(s))






'''#Next solution'''

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] != 'pop':
        eval('s.{}({})'.format(cmd[0], cmd[1]))
    else: s.pop()
print(sum(s))



