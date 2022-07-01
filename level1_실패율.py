# 실패율 : 스테이지 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수

# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열을 return
# 스테이지에 도달한 유저가 없으면 실패율은 0
# N+!은 마지막 스테이지까지 클리어한 사용자 수

N = 4
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
stages = [4,4,4,4,4]
stages.sort()  # 정렬

fail = {}
for i in range(1, N+1):
    length = len(stages)
    count = stages.count(i)

    if length == 0:
        fail[i] = 0
    else:
        fail[i] = (count/length)
    for j in range(count):
        stages.pop(0) # 개수만큼 제거

sorted_dict = sorted(fail.items(), key = lambda item: item[1], reverse = True)
result = [value[0] for value in sorted_dict]
print(result)

