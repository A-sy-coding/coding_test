# 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return하도록한다.
# sqrt(n)까지의 약수만 구하면 된다. --> 시간복잡도 감소
# ex) 24의 경우 sqrt(24) -> 1~4까지만 비교하면 된다.

left = 24
right = 27
answer = 0
for i in range(left, right+1):
    count = 0 # 약수의 개수를 세는 변수
    for j in range(1,int(i**(1/2))+ 1): # sqrt(n)만큼 반복
        if i%j == 0:  # 약수이면
            front = j
            back = i // j

            if front == back:  # 25 = 5*5의 경우 약수의 개수는 1개로 취급
                count +=1
            else:
                count += 2
    if count % 2 == 0:
        answer += i
    else:
        answer -= i

print(answer)

#######################
# 어떠한 수가 제곱의 곱으로 표현이 가능하다면 해당 수의 약수는 홀수가 된다.
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer