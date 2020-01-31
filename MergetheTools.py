def merge_the_tools(s, k):
    p = len(s)/k
    idx = 0
    subs = []
    for i in range(1, len(s)+1):
        if (i % p) == 0:
            subs.append(s[idx:i])
            idx = i

    from collections import OrderedDict
    [print("".join(OrderedDict.fromkeys(sub))) for sub in subs]




'''#Next solution'''

def merge_the_tools(s, k):
    p = len(s)/k
    idx = 0
    subs = []
    for i in range(1, len(s)+1):
        if (i % p) == 0:
            subs.append(s[idx:i])
            idx = i

    from collections import OrderedDict
    [print("".join(OrderedDict.fromkeys(sub))) for sub in subs]




'''#Next solution'''

def merge_the_tools(s, k):
    p = len(s)/k
    idx = 0
    subs = []
    for i in range(1, len(s)+1):
        if (i % p) == 0:
            subs.append(s[idx:i])
            idx = i

    from collections import OrderedDict
    [print("".join(OrderedDict.fromkeys(sub))) for sub in subs]




'''#Next solution'''

def merge_the_tools(s, k):
    p = len(s)/k
    idx = 0
    subs = []
    for i in range(1, len(s)+1):
        if (i % p) == 0:
            subs.append(s[idx:i])
            idx = i

    from collections import OrderedDict
    [print("".join(OrderedDict.fromkeys(sub))) for sub in subs]

