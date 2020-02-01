# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
s = input()

print(*((len(list(n)),int(c)) for c, n in itertools.groupby(s)))
    
