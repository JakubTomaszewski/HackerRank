def count_substring(string, sub_string):
    occ = 0
    for i in range(len(string)):
        if string[i:(i+len(sub_string))] == sub_string:
            occ+=1
    return occ




'''#Next solution'''

def count_substring(string, sub_string):
    occ = 0
    for i in range(len(string)):
        if string[i:(i+len(sub_string))] == sub_string:
            occ+=1
    return occ

