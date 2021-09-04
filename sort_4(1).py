N, K = map(int,input().split(' '))

A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))

A.sort()#오름차순
B.sort(reverse=True)#내림차순

for var in range(K):
    A[var],B[var] = B[var],A[var]

print(sum(A))
