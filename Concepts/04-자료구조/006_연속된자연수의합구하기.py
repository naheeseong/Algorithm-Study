import sys
input = sys.stdin.readline
N = int(input())
startIndex = 1
endIndex = 1
count = 1 # 항상 자기자신  포함
total = 1 # 1부터 시작함
while endIndex != N:
    if total == N:
        count += 1
        endIndex += 1
        total += endIndex
    elif total < N:
        endIndex += 1
        total += endIndex
    else:
        total -= startIndex
        startIndex += 1
print(count)