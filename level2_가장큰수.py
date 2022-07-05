# def solution(numbers):
#     answer = ''
#     numbers = [str(i)  for i in numbers]
    
#     from itertools import permutations
#     # case = list(permutations(numbers, len(numbers)))
#     # print([''.join(i) for i in case])
#     case = list(map(''.join, permutations(numbers,len(numbers)))) # 전체 경우의 수
#     answer = str(sorted([int(i) for i in case])[-1])
    
    
    
#     return answer

# print(solution([6,10,2]))

##########################
# 위의 수식은 시간초과가 발생하였다.
# 기수 정렬을 사용하면 해결 가능해 보인다.
# 일의자리 숫자부터 서로 비교하게끔 한다.
# numbers = [6,10,2]
numbers = [3, 30, 34, 5, 9]

number_str = list(map(str, numbers))

number_str.sort(key = lambda x : x*3 , reverse=True)
print(number_str)

print(str(int(''.join(number_str))))
# int로 감싸는 이유는 0000과 같은 문자가 있을 경우, 해당 문자를 int형으로
# 변경해주고, 다시 str 형태로 바꿔주도록 한다.
