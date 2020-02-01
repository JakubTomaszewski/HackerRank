import numpy as np

data = list(map(int,input().split()))

ar1 = np.array([list(map(int,input().split())) for i in range(data[0])])
ar2 = np.array([list(map(int,input().split())) for i in range(data[1])])

print(np.concatenate((ar1, ar2)))



