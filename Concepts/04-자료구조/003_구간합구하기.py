import sys

# 기본 input() 대비 속도가 훨씬 빠른 sys.stdin.readline으로 대체 (시간초과방지)
input = sys.stdin.readline
n, m = map(int,input().split())
A = list(map(int, input().split()))
S = [0]
tmp = 0
for i in A:
    tmp = tmp + i
    S.append(tmp)
for i in range(m):
    j, k = map(int, input().split())
    print(S[k]-S[j-1])