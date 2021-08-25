N, M, K = map(int, input().split(' '))
num_list= list(map(int,input().split(' ')))

num_list.sort()

print(num_list, type(num_list))


result = int(M/(K+1))* (num_list[-1]*K+num_list[-2])
print('result',int(M/(K+1)))
result += M%(K+1) *num_list[-1]
print('result',result)

print(result)