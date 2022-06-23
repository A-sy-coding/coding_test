# 조합을 생각하여 unique를 이용하여 중복되지 않는 값만 남게 구현
# 고유한 값만 남기고, 고유한 값의 개수에 따라 출력값을 수정한다.
nums = [3,3,3,2,2,4]

div_count = len(nums) // 2
unique = set(nums)

if div_count == len(unique):
    print(len(unique))
elif div_count > len(unique):
    print(len(unique))
else:
    print(div_count)

#######################3
# 위의 코드를 좀 더 줄이면 밑의 코드와 같다.
answer = min(len(nums)/2, len(set(nums)))