n = int(input())
list = []
for i in range(n):
    tmp = int(input())
    list.append(tmp)
for i in range(n-1):
    for j in range(n-i-1):
        if list[j] > list[j+1]:
            tmp = list[j]
            list[j] = list[j+1]
            list[j+1] = tmp
for item in list:
    print(item)