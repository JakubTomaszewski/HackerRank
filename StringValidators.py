if __name__ == '__main__':
    s = input()
    is_it = {i: False for i in range(5)}
for i in range(len(s)):
    if s[i].isalnum():
        is_it[0] = True
    if s[i].isalpha():
        is_it[1] = True
    if s[i].isdigit():
        is_it[2] = True
    if s[i].islower():
        is_it[3] = True
    if s[i].isupper():
        is_it[4] = True
        
for value in is_it.values():
    print(value)
    

