def swap_case(s):
    word = ''
    for letter in s:
        if letter.islower():
            word+=letter.upper()
        else:
            word+=letter.lower()
    return word




'''#Next solution'''

def swap_case(s):
    return ''.join(l.upper() if l.islower() else l.lower() for l in s)




'''#Next solution'''

def swap_case(s):
    word = ''
    for letter in s:
        if letter.islower():
            word+=letter.upper()
        else:
            word+=letter.lower()
    return word




'''#Next solution'''

def swap_case(s):
    return ''.join(l.upper() if l.islower() else l.lower() for l in s)

