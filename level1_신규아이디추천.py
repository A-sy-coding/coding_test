# new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "=.="
symbol = ['-','_','.']
lower_id = new_id.lower()

str = ""
for i in lower_id:
    if (i.isalpha()) or (i in symbol) or (i.isdigit()):
        str += i
# 3단계  --> .이 두개 이상이면 하나로 만들기 -> 배열 두개를 이용하여 중복 제거
str1 = ""
for i in range(len(str)):
    if i==0:
        str1 += str[i]
    elif str1[-1] == '.' and str[i] == '.':
        continue
    else:
        str1 += str[i]


# 4단계 --> .이 처음이나 끝에 존재하면 제거
if str1[0] == '.':
    str1 = str1[1:]

if str1 != "":
    if str[-1] == ".":
        str1 = str1[:-1]


# 5단계 -> 빈 문자열이면, new_id에 "a"를 대입
if str1 == "":
    str1 += "a"

# 6단계 -> 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 제거
if len(str1) >= 16:
    str1 = str1[:15]
    if str1[-1] == '.':
        str1 = str1[:-1]

# 7단계 -> 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될때까지 반복
if len(str1) <= 2:
    while len(str1) < 3:
        str1 += str1[-1]

print(str1)

########################
# 3단계를 밑의 과정으로도 풀 수 있음을 확인
# while '..' in answer:
#         answer = answer.replace('..', '.')