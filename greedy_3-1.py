print('행 갯수:',end=' ')
row = int(input())#두번째 반복 횟수
print('열 갯수:',end=' ')
column = int(input())#첫번째 반복 횟수

table = []
num_list = []

for var1 in range(row):
    for var2 in range(column):
        print(f'{var1+1}번째 행 {var2+1}번째 숫자-> ',end='')
        num_list.append(int(input()))
    table.append(num_list)
    num_list=[]

greatest_small_index = 0

for var1 in range(1,len(table)):
    if min(table[var1-1])< min(table[var1]):
        greatest_small_index = var1

print(f'{greatest_small_index+1}번째 행')
print(table[greatest_small_index])