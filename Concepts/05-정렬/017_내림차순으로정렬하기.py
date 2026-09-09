import sys
print = sys.stdout.write
arr = list(input())
for i in range(len(arr)):
    # max 찾기
    Max = i
    for j in range(i,len(arr)):
        if arr[Max] < arr[j]:
            Max = j
    tmp = arr[Max]
    arr[Max] = arr[i]
    arr[i] = tmp
for i in arr:
    print(i, end="")