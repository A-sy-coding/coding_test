# 해당 문제풀이는 빈 배열을 만들고 해당 배열을 빈도를 세는 것으로 이용하였다.
def solution(numbers):
    x = [0] * 10
    answer = 0

    for i in numbers:
        x[i] += 1

    for i in range(len(x)):
        if x[i] == 0:
            answer += i

    return answer

#####################
# set을 이용하여 중복된 부분을 제거하는 방법도 존재
# 0~9까지의 총 합에서 주어진 조건의 전체 합을 빼는 방법도 존재