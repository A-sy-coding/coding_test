# 문자열을 압출할 떄 가장 최소의 길이를 갖도록 문자열 압축
# 몇개로 묶어서 나눠야지 압축률이 가장 좋은가?

s = "aabbaccc"

length = []
result = ""

if len(s) == 1:
    print(1)

for cut in range(1, len(s) // 2 + 1):
    count = 1
    tempStr = s[:cut]
    for i in range(cut, len(s), cut):
        if s[i:i + cut] == tempStr:
            count += 1
        else:
            if count == 1:
                count = ""
            result += str(count) + tempStr
            tempStr = s[i:i + cut]
            count = 1

    if count == 1:
        count = ""
    result += str(count) + tempStr
    length.append(len(result))
    result = ""

# print(length)



# # 예를 들어, 길이가 11이면, 5까지는 묶음이 가능하고, 6부터는 묶음이 불가능하다.
# length = len(s) // 2   # 문자열의 길이 --> 문자열의 길이의 절반값까지만 묶음으로 나눌 수 있다.
#
# result = []
# string = ''
#
# if len(s) == 1:
#     print(1)
#
# for i in range(1, length+1): # 묶음을 length 길이까지 밖에 못 묶는다.
#     count =1  # 연속으로 중복된 개수 세기
#     temp = s[:i]  # 가장 처음 묶음 단어 설정
#     for j in range(i, len(s),i):
#         if s[j:j+i] == temp:
#             count += 1
#         else:
#             if count == 1:
#                 count = ''
#             string += str(count) + temp
#             temp = s[i:i+j]
#     if count == 1:
#         count = ""
#     string += str(count) + temp
#     result.append(len(string))
#     string = ""
#
# print(result)

##########################
# zip을 이용하여 중복되는 두개의 값들을 서로 비교할 수 있다.
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1

    for word, cnt in res:
        print(word, cnt)
        if cnt > 1:
            print(len(word) + (len(str(cnt))))
        else:
            print(0)
    print(sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res))
    print('------')
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])


a = [
    "aabbaccc",
    # "ababcdcdababcdcd",
    # "abcabcdede",
    # "abcabcabcabcdededededede",
    # "xababcdcdababcdcd",
    #
    # 'aaaaaa',
]

for x in a:
    print(solution(x))