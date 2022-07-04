# expression = "100-200*300-500+20"
expression = "50*6-3*2"

string = ''
split = []
symbol = []
for s in expression:
    if s.isdigit():
        string += s
    else:
        split.append(string)
        split.append(s)
        symbol.append(s)
        string = ''
split.append(string)

from itertools import permutations
comb = list(permutations(set(symbol), len(set(symbol))))

answer= []
for symbol in comb:  # ('*','-','+')
    split_list = split.copy()

    for s in symbol:
        indexs = [i for i, v in enumerate(split_list) if v == s]

        for count in range(len(indexs)):
            index = split_list.index(s)

            if s == '-':
                value = int(split_list[index - 1]) - int(split_list[index + 1])

                del split_list[index - 1: index + 2]  # 3개 값 삭제
                split_list.insert(index - 1, value)

            elif s == '*':
                value = int(split_list[index - 1]) * int(split_list[index + 1])

                del split_list[index - 1: index + 2]  # 3개 값 삭제
                split_list.insert(index - 1, value)

            elif s == '+':
                value = int(split_list[index - 1]) + int(split_list[index + 1])

                del split_list[index - 1: index + 2]  # 3개 값 삭제
                split_list.insert(index - 1, value)
    # print(split_list)
    answer.append(abs(split_list[0]))

print(max(answer))
