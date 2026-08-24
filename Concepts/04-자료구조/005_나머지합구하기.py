import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
S = []
tmp = 0
cnt = 0
C = [0] * M
for i in arr:
    tmp = (tmp + i) % M
    if tmp == 0:
        cnt += 1
    C[tmp] += 1
# print(cnt)
for i in C:
    if i != 0:
        tmp = i*(i-1)//2
        cnt += tmp
print(cnt)