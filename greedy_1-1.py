user = input()
user = float(user)
dic = {500: 0, 100 : 0, 50:0, 10:0}

dic[500] = int(user/500)
user = user%500

dic[100] = int(user/100)
user = user %100

dic[50] = int(user/50)
user = user%50

dic[10] = int(user/10)
user = user%10

print(dic)