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
