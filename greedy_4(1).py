N, K = map(int,input().split(' '))
print(type(N))

count =0


while N !=1:
    if N%K ==0:
        N = N/K
        count += 1
    else:
        N = N-1
        count += 1
print('반복 횟수: ',count)
