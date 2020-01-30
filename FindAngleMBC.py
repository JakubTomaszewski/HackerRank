# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())


print(str(round(math.degrees(math.asin((((ab**2 + bc**2)**(0.5))/2)/bc))))+'°')



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab = int(input())
bc = int(input())

if ab == bc:
    print(str(round(math.degrees(math.asin((((ab**2 + bc**2)**(0.5))/2)/bc))))+'°')
else:
    res = (ab**2)/(bc*((ab**2 + bc**2)**(0.5)))
    deg = math.degrees(math.asin(res))
    print(str(round(res))+'°')



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
ab = float(input())
bc = float(input())


print(str(round(math.degrees(math.asin((((ab**2 + bc**2)**(0.5))/2)/bc))))+'°')



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 

ab = int(input()) 
bc = int(input()) 
print(str(int(round(math.degrees(math.atan2(ab,bc)))))+'°')



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 

ab = int(input()) 
bc = int(input()) 
print(str(int(round(math.degrees(math.atan2(ab,bc)))))+'°')
