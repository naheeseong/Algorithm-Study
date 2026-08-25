import sys
input = sys.stdin.readline
# 수열의 크기 입력받기
n = int(input())
# 수열 입력받기
A = list(map(int, input().split()))
# 오큰수 저장하는 배열
answer = [0]*n
# 스택
mystack = []
# 수열 인덱스 0~n-1 검사
for i in range(n):
    # 스택이 비어있지않고 스택의 top보다 현재 인덱스의 수열의 값이 큰 동안 반복문 실행
    while mystack and A[mystack[-1]] < A[i]:
        # 오큰수 저장하기
        answer[mystack.pop()] = A[i]
    mystack.append(i)
# 수열 모두 검사했는데 스택이 남아있으면 해당 인덱스 위치에 -1 저장
while mystack:
    answer[mystack.pop()] = -1
# 공백두고 리스트 출력
print(*answer)