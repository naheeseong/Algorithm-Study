n = int(input())
A = [0]*n
for i in range(n):
    A[i] = int(input())
stack = []
answer = []
result = True
num = 1
for i in range(n):
    if A[i] >= num:
        while A[i] >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:
        tmp = stack.pop()
        if tmp != A[i]:
            print("NO")
            result = False
            break
        else:
            answer.append('-')
if result:
    for i in answer:
        print(i)