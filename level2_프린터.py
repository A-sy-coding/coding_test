priorities = [1, 1, 9, 1, 1, 1]
location = 0

answer = 0
# stack를 이용한다. --> list 사용

# stack = [i for i in range(len(priorities))]
# store = []
#
# while stack:
#     flag = 0
#     max_value = max(priorities)
#     for i, p in enumerate(priorities):
#         if p != max_value:
#             temp = priorities[0]
#             priorities.pop(0)
#             priorities.append(temp)
#             temp1 = stack[0]
#             # print(temp, temp1)
#             stack.pop(0)
#             stack.append(temp1)
#             break
#         else:
#             priorities.pop(0)
#             result = stack[0]
#             stack.pop(0)
#
#             store.append(result)
#             break
#     # print(priorities, stack, store)
#
#     if len(store) > 0 and store[-1] == location:
#         answer = store.index(store[-1]) + 1
#         break

###############################
# any를 이용하여 구하는 방법

stack = [(i,p) for i,p in enumerate(priorities)]
print(stack)

while 1:
    cur = stack.pop(0)
    if any(cur[1] < i[1] for i in stack):
        stack.append(cur)
    else:
        answer += 1
        if cur[0] == location:
            break

print(answer)