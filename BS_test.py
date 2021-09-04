def binary_sort(start, end, target, array):#
    count =0
    while start<=end:
        mid = (start+end)//2
        count +=1
        print('count',count)
        if array[mid] == target:
            return mid
        if array[mid]<target:
            start=mid+1
        if array[mid]>target:
            end = mid-1
    return None


n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

print ('n',n, 'target',target, )
print(array)
print(binary_sort(0,n-1,target,array))