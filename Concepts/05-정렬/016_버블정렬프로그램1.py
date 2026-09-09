n = int(input())
arr = []
for i in range(n):
    tmp = int(input())
    arr.append((tmp, i))
sortedArr = sorted(arr)
Max = 0
for i in range(n):
    # 정렬 전 인덱스 - 정렬 후 인덱스 (왼쪽으로 이동한 최댓값 == 바깥 루프의 시행 횟수)
    if Max < sortedArr[i][1]-i:
        Max = sortedArr[i][1]-i
print(Max+1)