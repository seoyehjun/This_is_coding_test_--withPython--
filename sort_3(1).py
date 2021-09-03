#오름차수
import operator

num = int(input())
dic = {}

for var in range(num):
    user_input = input().split(' ')
    dic[user_input[0]] = int(user_input[1])
    
result = sorted(dic.items(), key=operator.itemgetter(1))

print(result)
