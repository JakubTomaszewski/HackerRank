def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)




'''#Next solution'''

def mutate_string(string, position, character):
    str = ''
    for i in range(len(string)):
        if i==position:
            str += character
        else:
            str += string[i]
    return str
