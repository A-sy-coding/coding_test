# s = "one4seveneight"
s = "123"

digit_name = ['zero','one','two','three','four','five','six','seven','eight','nine']
digit_dict = {}

# 사전으로 key-value 쌍으로 묶기
for i in range(len(digit_name)):
    digit_dict[digit_name[i]] = i

for i in digit_name:
    first_index = s.find(i)  # 문자가 존재하면 인덱스 반환
    last_index = len(i)

    if first_index == -1:  # 해당 문자가 없으면 그 다음 for문으로 이동
        continue

    word = s[first_index : first_index+last_index] # 문자 숫자 저장
    s = s.replace(word, str(digit_dict[word])) # 값 변환

print(s)

######################
# 딕셔너리의 items()를 사용하여 문자열을 수정할 수 있다.
# 위에서는 find함수를 사용하여 값들의 위치를 찾았지만,
# 밑의 코드는 find함수가 없어도 replace 함수자체가 없는 것들을 알아서 걸러준다.

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)