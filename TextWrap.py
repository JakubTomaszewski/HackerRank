

def wrap(string, max_width):
    word = ''
    i = 1
    for letter in string:
        if i%max_width == 0:
            word += str(letter)+'\n'
        else:
            word += str(letter)
        i+=1
    return word




'''#Next solution'''



def wrap(string, max_width):
    word = ''
    i = 1
    for letter in string:
        if i%max_width == 0:
            word += str(letter)+'\n'
        else:
            word += str(letter)
        i+=1
    return word

