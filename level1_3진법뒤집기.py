def solution(n):
    answer = 0

    # 3으로 나눈 나머지를 이용한다.
    temp = []  # 뒤집은 값 저장
    while n != 0:
        div = n % 3  # 3으로 나눈 나머지
        temp.append(div)
        n = n // 3

        # 10진법 계산
    for i in range(len(temp)):
        v = temp[len(temp) - 1 - i]
        answer += (v * 3 ** i)
    return answer

#################
# 3진법을 구하기 위해서는 십진수를 3으로 나눈 나머지를 이용하여 구할 수 있다.
################

# int 내장 함수를 이용하여 3진법을 십진법으로 구할 수 있다.
n = 45

tmp = ''
while n:
    tmp += str(n%3)
    n = n // 3

print(tmp)

answer = int(tmp,3)  # int에 삼진법을 십진법으로 반환해주는 것이 존재한다.
print(answer)