# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
date = list(map(int,raw_input().split()))
print(list(calendar.day_name)[calendar.weekday(date[2],date[0], date[1])].upper())
