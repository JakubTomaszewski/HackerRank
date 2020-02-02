# Enter your code here. Read input from STDIN. Print output to STDOUT
shoes = int(input())
sizes = input().split()
customers = int(input())
earnings = 0

for i in range(customers):
    offer = input().split()
    if offer[0] in sizes:
        earnings += int(offer[1])
        sizes.remove(offer[0])
    
print(earnings)

