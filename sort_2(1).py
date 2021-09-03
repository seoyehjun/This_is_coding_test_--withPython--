num = int(input())
num_list = []
sorted_list = []
result =[]

for var in range(num):
    num_list.append(int(input()))

for var in range(num):
    sorted_list = [0]*1000

for var in range(num):
    sorted_list[num_list[var]] +=1

for var1 in range(len(sorted_list)-1,-1,-1):
    for var2 in range(sorted_list[var1]):#해당 인덱스숫자와 같은 숫자의 갯수만큼 반복
        result.append(var1)#인덱스 값을 요소로 쓴다 ㅋㅋ

print(result)