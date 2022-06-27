# 더하고 뺀값을 전부 저장

numbers = [4, 1, 2, 1]
target = 4

y = [0]  # 더하고 뺀값을 저장 -> 모든 케이스에 대한 값 저장
for num in numbers:
    temp = []
    for i in y:
        temp.append(i + num)
        temp.append(i - num)
    y = temp  # 구한값을 다시 정의

answer = 0
for value in y:
    if target == value:
        answer += 1

print(answer)

###########################
# 깊이 우선 탐색으로 코드

answer = 0
def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer

