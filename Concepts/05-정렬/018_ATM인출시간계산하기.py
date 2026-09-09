n = int(input())
A = list(map(int, input().split()))

for i in range(1, n):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1,-1,-1):
        if A[j] < A[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i-1,insert_point-1,-1):
        A[j+1] = A[j]
    A[insert_point] = insert_value
# 구간 합 구현 S[i] = S[i-1] + A[i]
S = [0]*n
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]
sum = 0
for i in S:
    sum += i