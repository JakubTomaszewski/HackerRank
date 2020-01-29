if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

def return_max(array):
    array = list(array)
    maximum = max(array)
    while max(array) == maximum:
        array.remove(max(array))
    return max(array) 
            

print(return_max(arr))
