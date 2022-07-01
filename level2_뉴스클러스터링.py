str1 = 'FRANCE'
str2 = 'french'

str1 = str1.lower()
str2 = str2.lower()

str1_set = []
str2_set = []
for i in range(len(str1)-1):
    temp = str1[i] + str1[i+1]
    if temp.isalpha() and len(temp) == 2: # 공백도 제거
        str1_set.append(temp)

for i in range(len(str2)-1):
    temp = str2[i] + str2[i+1]
    if temp.isalpha() and len(temp) == 2: # 공백도 제거
        str2_set.append(temp)


def get_intersection(str1_set, str2_set):
    temp = [] # 임의값 저장하는 리스트
    result = []
    for i in str1_set:
        if i in temp:
            continue
        else:
            temp.append(i)
            str1_count = str1_set.count(i)
            str2_count = str2_set.count(i)
            min_count = min(str1_count, str2_count)
            result.extend([i]*min_count)
    return result
def get_union(str1_set, str2_set):
    str1_temp = str1_set.copy()
    str1_result = str1_set.copy()

    for i in str2_set:
        if i not in str1_temp:
            str1_result.append(i)
        else:
            str1_temp.remove(i)

    return str1_result

print(str1_set)
print(str2_set)

if len(str1_set) == 0 and len(str2_set) == 0:
    answer = 1 * 65536
elif len(str1_set) == 0 or len(str1_set) == 0:
    answer = 0
else:
    intersection = get_intersection(str1_set, str2_set)
    union = get_union(str1_set, str2_set)
    answer = int(len(intersection) / len(union) * 65536)

print(answer)


########################
# 고유한 합집합을 구한뒤, 개수에 따라 값들을 추가하였다.
def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]

    tlist = set(list1) | set(list2)
    print(set(list1))
    print(set(list2))
    print(tlist)
    res1 = [] #합집합
    res2 = [] #교집합

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))

        answer = int(len(res2)/len(res1)*65536)
        return answer

    else:
        return 65536

solution(str1, str2)