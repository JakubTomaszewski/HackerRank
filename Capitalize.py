

# Complete the solve function below.
def solve(s):
    s= s.capitalize()
    for i in range(len(s)):
        if s[i] == ' ':
            s = s.replace(s[i+1], s[i+1].upper())
            break
    return s




'''#Next solution'''



# Complete the solve function below.
def solve(s):
    s= s.capitalize()
    for i in range(len(s)):
        if s[i] == ' ':
            s = s.replace(s[i+1], s[i+1].upper())
    return s




'''#Next solution'''



# Complete the solve function below.
def solve(s):
    return ' '.join(word.capitalize() for word in s.split())




'''#Next solution'''



# Complete the solve function below.
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

