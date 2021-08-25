N = int(input())

count =0
for var in range(N+1):
    if '3' in str(var):
        count +=3600
        continue
    for var1 in range(60):
        if '3' in str(var1):
            count += 60
            continue
        for var2 in range(60):
            if '3' in str(var2):
                count += 1

print(count)