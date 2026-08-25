import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()
i = 0
j = N-1
total = arr[i] + arr[j]
count = 0
while i != j:
    if total == M:
        count += 1
        i += 1
        total = arr[i] + arr[j]
    elif total < M:
        i += 1
        total = arr[i] + arr[j]
    else:
        j -= 1
        total = arr[i] + arr[j]
print(count)

'''
6
9
2 7 4 1 5 3
'''