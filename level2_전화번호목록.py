def solution(phone_book):
    answer = True

    # 문자열을 sort하면, 문자순으로 정렬되게 된다.
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # if phone_book[i] in phone_book[i+1]:
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
                answer = False
                break

    return answer
###################3
# 문자로 정렬하고 처음부분만 서로 비교하면 구할 수 있다..
###################

# startswith를 이용하여 답 구하기
phone_book = ["119", "97674223", "1195524421"]

answer = True
phone_book.sort() # 값 문자를 기준으로 정렬
# print(phone_book)
for a,b in zip(phone_book, phone_book[1:]):
    # print(a,b)
    if b.startswith(a):
        answer = False
        break
# print(answer)

############################

# 정석 hash를 이용해 정답 출력
hash = {}
for number in phone_book:
    hash[number] = 1
print(hash)

for number in phone_book:
    temp = ''
    for num in number:
        temp += num
        print(temp)
        print(number)
        if temp in hash and temp != number:
            answer= False
            print(hash)
