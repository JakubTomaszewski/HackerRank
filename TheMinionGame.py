def minion_game(string):
    # your code goes here
    pts_kevin = 0
    pts_stuart = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            for i in range(len(s[i:])):
                pts_kevin += 1
        else:
            for i in range(len(s[i:])):
                pts_stuart += 1
    if max(pts_kevin, pts_stuart) == pts_stuart:
        print('Stuart', pts_stuart)
    else:
        print('Kevin', pts_kevin)
    '''
    gets a string
    iters through for i in range len(string)
    if letter is vowel is starts getting all substrings
    new_sub_pts = len(string[letter_index:]) 
    '''



'''#Next solution'''

def minion_game(string):
    # your code goes here
    pts_kevin = 0
    pts_stuart = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            for i in range(len(s[i:])):
                pts_kevin += 1
        else:
            for i in range(len(s[i:])):
                pts_stuart += 1
    if pts_kevin == pts_stuart:
        print('Draw')
    elif max(pts_kevin, pts_stuart) == pts_stuart:
        print('Stuart', pts_stuart)
    else:
        print('Kevin', pts_kevin)
    '''
    gets a string
    iters through for i in range len(string)
    if letter is vowel is starts getting all substrings
    new_sub_pts = len(string[letter_index:]) 
    '''



'''#Next solution'''

def minion_game(string):
    # your code goes here
    pts_Kevin = 0
    pts_Stuart = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            pts_Kevin += (len(string)-i)
        else:
            pts_Stuart += (len(string)-i)
    if pts_Kevin > pts_Stuart:
        print('Kevin', pts_Kevin)
    elif pts_Stuart > pts_Kevin:
        print('Stuart', pts_Stuart)
    else:
        print('Draw')
