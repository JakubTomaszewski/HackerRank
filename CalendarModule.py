# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
date = input().split()

print(calendar.weekday(date[2],date[0], date[1]))



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
date = list(map(int,raw_input().split()))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(days[calendar.weekday(date[2],date[0], date[1])].upper())



'''#Next solution'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
date = list(map(int,raw_input().split()))
print(list(calendar.day_name)[calendar.weekday(date[2],date[0], date[1])].upper())
