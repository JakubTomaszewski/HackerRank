# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    chars = input().split()
    try:
        print(int(chars[0])//int(chars[1]))
    except ZeroDivisionError as z:
        print('Error Code:', z)
    except ValueError as v:
        print('Error Code:', v)
        

