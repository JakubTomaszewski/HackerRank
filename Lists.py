if __name__ == '__main__':
    N = int(input())
    l=[]
for line in range(N):
    x = input()
    if x.split()[0] == 'insert':
        l.insert(int(x.split()[1]), int(x.split()[2]))
    elif x.split()[0] == 'remove':
        l.remove(int(x.split()[1]))
    elif x.split()[0] == 'append':
        l.append(int(x.split()[1]))
    elif x.split()[0] == 'sort':
        l.sort()
    elif x.split()[0] == 'reverse':
        l.reverse()
    elif x.split()[0] == 'pop':
        l.pop()
    else:
        print(l)

