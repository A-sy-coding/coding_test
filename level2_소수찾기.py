from itertools import permutations
numbers = '0117'    

case_list = []
for i in range(len(numbers)):
    case = list(permutations(list(numbers), i+1))
    for num in case:
        case_list.append(num)
        
# case_list = set(case_list)  # 중복된 값들은 제거
case_int = set([int(''.join(i)) for i in case_list])

answer = 0

# print(case_int)
for num in case_int:
    # print(num)
    # print(int(num**0.5))   
    if num == 1:
        continue
    flag = 1  # 소수 여부 파악
    for i in range(2,num): # 숫자의 제곱근 까지만 봐도 소수를 판별할 수 있다.
                            # int(num ** 0.5) + 1 까지만 확인하면 시간복잡도가 조금 더 줄어든다.
        if num % i == 0:
            flag = 0
            break
    if flag:
        answer += 1
# print(answer)


#####################
# 에라토스테네스 체를 이용하여 소수 판별이 가능하다.
a = set()
for i in range(len(numbers)):
    a |= set(map(int,map(''.join,permutations(list(numbers), i + 1))))  # set의 합집합 구하기
print(a)
a -= set(range(0,2))  # 0과 1은 집합에서 제거
print(a)

for i in range(2, int(max(a) ** 0.5)+1):
    a -= set(range(i * 2, max(a) + 1, i))  # i의 배수들은 소수가 아니므로 제거한다.

print(a)



##################
x = set([1,2,3])
y = set([1,5,6])
# x | y는 합집합을 구할 수 있고, x & y는 교집합을 구할 수 있게 된다.
# print(x&y)
####################