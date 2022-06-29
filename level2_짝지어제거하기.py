s = 'cdcd'

# unique_s = set(s)  # 고유 문자값만 가져오기
#
# answer = 0
# while 1:
#     count = 0
#     for i in unique_s:
#         temp = i + i
#         if temp in s:
#             s = s.replace(temp, '')
#             count += 1
#
#     if len(s) == 0:
#         answer = 1
#         break
#
#     if count == 0:
#         break
#
# print(answer)

#######################
### 스택을 이용하면 for문 하나로 해결이 가능합니다.
s = 'cdcd'


stack = []
stack.append(s[0])

for i in s[1:]:

    if len(stack) > 0 and stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)

print(stack)
if len(stack) == 0 :
    answer = 1
else:
    answer = 0

print(answer)
