import sys
input = sys.stdin.readline
myArr = [0]*4
checkArr = [0]*4
matched = 0
# 문자 추가 후 검사 
def myadd(c):
    global myArr, checkArr, matched
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            matched += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            matched += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            matched += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            matched += 1
# 문자 제거 후 검사
def myremove(c):
    global myArr, checkArr, matched
    if c == 'A':
        if myArr[0] == checkArr[0]:
            matched -= 1
        myArr[0] -= 1
    elif c == 'C':
        if myArr[1] == checkArr[1]:
            matched -= 1
        myArr[1] -= 1
    elif c == 'G':
        if myArr[2] == checkArr[2]:
            matched -= 1
        myArr[2] -= 1
    elif c == 'T':
        if myArr[3] == checkArr[3]:
            matched -= 1
        myArr[3] -= 1

S, P = map(int, input().split())
A = input()
checkArr = list(map(int, input().split()))
result = 0
# 조건을 충족한 dna 문자는 미리 더해놓기
for i in range(4):
    if checkArr[i] == 0:
        matched += 1
# 처음 부분 문자열 검사
for i in range(P):
    myadd(A[i])
if matched == 4:
        result += 1
# 슬라이딩 윈도우
for i in range(P, S):
    j = i-P
    myadd(A[i])
    myremove(A[j])
    if matched == 4:
        result += 1
print(result)