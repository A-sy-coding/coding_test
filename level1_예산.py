d = [1,3,2,5,4]
# d = [2,2,3,3]
budget = 9
d.sort() # 크기 순으로 정렬

price = 0
count = 0
for i in d:
    price += i  # 작은것부터 채우기
    count += 1
    if price > budget:
        price -= i  # 그 전의 가격으로 반환
        count -= 1
        break


if (budget - price) in d[count:]:
    count += 1

print(count)