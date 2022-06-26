
progresses = [93, 30, 55]  # 왼쪽부터 먼저 배포되어야 한다.
speeds = [1, 30, 5]

# count = 0  # 처리완료된 기능 개수
# day = [0] * len(progresses) # 걸린 날짜 세기
# days = [0] * len(progresses) # 최종 날짜 구하기
# flag = [1] * len(progresses)
# while count < len(progresses):
#     for index, (pg, sp) in enumerate(zip(progresses, speeds)):
#         progresses[index] += speeds[index] # progress 증가
#         day[index] += 1  # 날짜 증가
#
#         if progresses[index] >= 100:
#             if flag[index]:
#                 days[index] = day[index]
#                 count += 1
#             flag[index] = 0
# answer = []
# cmp = days[0]
#
# c = 0
# for i in days:
#     if i <= cmp:
#         c += 1
#     else:
#         answer.append(c)
#         c = 1
#         cmp = i
# answer.append(c)

# print(answer)

##################################
# 즉, 위의 코드는 시간복잡도가 O(n^2)정도 되지만,
# 밑의 코드는 좀더 시간복잡도가 줄어들게 된다.
# time은 초기화가 되지 않기 때문에 계속 값은 증가하게 된다.
print(progresses)
print(speeds)
answer = []
time = 0
count = 0
while len(progresses) > 0:
    print(progresses[0] + time * speeds[0])
    if (progresses[0] + time * speeds[0]) >= 100:
        progresses.pop(0)
        speeds.pop(0)
        count += 1
    else:
        # print(count, progresses[0])
        if count > 0:
            answer.append(count)
            count = 0
        time += 1
answer.append(count)
print(answer)