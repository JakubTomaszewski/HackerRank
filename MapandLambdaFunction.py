cube = lambda x: x**3 

def fibonacci(n):
    fib = [0,1]
    for i in range(1,(n-1)):
        fib.append(fib[i-1]+fib[i])
    return fib

    # return a list of fibonacci numbers




'''#Next solution'''

cube = lambda x: x**3 

def fibonacci(n):
    fib = [0,1]
    for i in range(1,(n-1)):
        fib.append(fib[i-1]+fib[i])
    return fib

    # return a list of fibonacci numbers




'''#Next solution'''

cube = lambda x: x**3 

def fibonacci(n):
    fib = [0]
    if n>1:
        fib.append(1)
    for i in range(1,(n-1)):
        fib.append(fib[i-1]+fib[i])
    return fib

    # return a list of fibonacci numbers




'''#Next solution'''

cube = lambda x: x**3 

def fibonacci(n):
    fib = [0]
    if n>1:
        fib.append(1)
    if n==0:
        return []
    for i in range(1,(n-1)):
        fib.append(fib[i-1]+fib[i])
    return fib

    # return a list of fibonacci numbers

