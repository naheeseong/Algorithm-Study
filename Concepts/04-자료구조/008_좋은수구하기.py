import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr.sort
count = 0
for i in range(N):
    k = arr[i]
    i = 0
    j = N-1
    total = arr[i] + arr[j]
    flag = 0
    while i < j:
        if total < k:
            i += 1
            total = arr[i] + arr[j]
        elif total > k:
            j -= 1
            total = arr[i] + arr[j]
        else:
            count += 1
            break
print(count)


'''
10
1 2 3 4 5 6 7 8  9 10
'''