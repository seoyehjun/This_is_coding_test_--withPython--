
array = [3,2,1,4,5,3,2,6,2,8,9]


for var in range(1,len(array)):
    min_index = var
    for var2 in range(var,0,-1):
        if array[min_index]>array[var2]:
            