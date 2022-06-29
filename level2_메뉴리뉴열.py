orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]


from itertools import  combinations
answer = []
split_list = []
for iter in course:
    temp = {}
    for order in orders:

        if len(order) < iter:
            continue

        comb = list(combinations(order,iter))
        for x in comb:
            sorted_x = "".join(sorted(x))
            if sorted_x in temp:
                temp[sorted_x] += 1
            else:
                temp[sorted_x] = 1
    # print(temp)
    for key,value in temp.items():
        if value == max(temp.values()) and max(temp.values()) != 1:
            split_list.append(key)

for i in split_list:
    string = ''
    for j in i:
        string += j
    answer.append(string)

answer.sort()
# print(answer)

################################
# collections 라이브러리에서 Counter를 이용하면 더 간단히 해결 가능하다.
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()

        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]