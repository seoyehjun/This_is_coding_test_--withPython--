def binary_search(start, end, target, array):
    if start>end:
        return None

    mid = start+end//2
    
    if array[mid]==target:
        return mid
    elif target<array[mid]:
        #호출한 해당 함수의 리턴값을 리턴한다
        return binary_search(start,mid-1,target,array)
    elif array[mid]<target:
        #호출한 해당 함수의 리턴값을 리턴한다.
        return binary_search(mid+1,end, target,array)
