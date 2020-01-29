def print_formatted(number):
    # your code goes here
    #for i in range(1,number+1):
        #print(str(i).rjust(number),str(oct(i))[2:].rjust(number),str(hex(i))[2:].rjust(number),str(bin(i))[2:].rjust(number),sep=' ')   n = int(raw_input())
    
    width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))




 

