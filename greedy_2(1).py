N, M, K = input().split(' ')
num_list = input().split(' ')
num_list = list(map(int,num_list))
num_list.sort()
print(num_list, type(num_list))

result =0
count1 =0

while True:
    for var1 in range(int(K)):
        if count1>=int(M):
            break
        result += num_list[-1]
        count1 += 1
    if count1>=int(M):
            break        
    result += num_list[-2]
    count1 += 1



print('count1',count1)

print(result)