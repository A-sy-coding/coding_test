# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s = "{{20,111},{111}}"
# s = "{{123}}"

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
# s = s[1:-1]
# s = s.split(',')
#
# print(s)
# temp = []
# union = []
# for i in s:
#     if '}' in i and '{' in i:
#         temp.append(i[1:-1])
#         union.append(temp)
#         temp = []
#     elif '{' in i:
#         temp.append(i[1:])
#     elif '}' in  i:
#         temp.append(i[:-1])
#         union.append(temp)
#         temp = []
#     else:
#         temp.append(i)
# sort_union = sorted(union, key = lambda x : len(x))
#
#
# add_list = []
# answer = []
# for v in sort_union:
#     for i in v:
#         if i in answer:
#             continue
#         else:
#             answer.append(i)
# result = [int(a) for a in answer]
# print(result)

#########################
# pashing을 좀 더 잘할 때 코드 구현
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
print(s)
s1 = s.lstrip('{').rstrip('}').split('},{')
print(s1)
new_s = []
for i in s1:
    new_s.append(i.split(','))
print(new_s)

new_s.sort(key = len)
print(new_s)

answer=  []
for i in new_s:
    for j in range(len(i)):
        if int(i[j]) not in answer:
            answer.append(int(i[j]))
print(answer)