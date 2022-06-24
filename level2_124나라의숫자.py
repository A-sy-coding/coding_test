# 자연수만 존재
# 1,2,4 숫자만 사용

# 이진법처럼 몫과 나머지를 구하여 124로 변경
# 3을 계속 나누어 값을 변환한다.

n = 4
answer = ''
value = {1: '1', 2: '2', 0: '4'}

x = (n - 1) // 3  # 몫 --> 만약 3보다 크면 3으로 계속 나누어야 한다.
y = n % 3  # 나머지 --> 더이상 나눌 필요 없음

trans = []

if x == 0:
    trans.append(value[y])
elif x < 3:
    trans.append(value[y])
    trans.append(value[x])
else:
    trans.append(value[y])
    while x >= 3:
        print(x)
        temp_div = x % 3
        trans.append(value[temp_div])
        x = (x - 1) // 3
        print(x)
    if x >= 1:
        trans.append(value[x])

for i in range(len(trans)):
    answer += trans[len(trans) - i - 1]

print(answer)

##################3
# 위의 코드는 시간초과로 인해 실패
# [::-1]를 이용하면 역순으로 문자열을 읽을 수 있다.
def solution(n):
    answer = ''
    while n:
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]