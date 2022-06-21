record = ["Enter uid12 AN","Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan",  "Leave uid12"]

result_data = {}  # key가 고유id이고, value가 이용자 이름으로 설정
leave_id = {}  # 나간 user id 저장

# 최종 변경 된 아이디를 딕셔너리에 저장
for info in record:
    split_info = info.split()
    cond = split_info[0]  # enter or leave or change

    if cond == 'Enter':
        id = split_info[1]
        user = split_info[2]
        result_data[id] = user
    elif cond == 'Leave':
        id = split_info[1]  # id값만 가지고 있다.
        leave_id[id] = result_data[id]
        del(result_data[id])  # 삭제
    elif cond == "Change":
        id = split_info[1]
        user = split_info[2]
        result_data[id] = user


# 최종 변경된 값을 가지고 다시 for문을 통해 출력값 출력
result = []  # 최종 메세지들을 저장하는 리스트
for info in record:
    split_info = info.split()
    cond = split_info[0]  # enter or leave or change

    if cond == 'Enter':
        id = split_info[1]

        # enter도 이미 나간 사람이 다시 들어오지 않는다면 enter를 출력할 때 result_data에 id값이 존재하지 않게 된다.
        if id not in result_data:
            result.append("{}님이 들어왔습니다.".format(leave_id[id]))
        else:
            result.append("{}님이 들어왔습니다.".format(result_data[id]))

    elif cond == 'Leave':
        id = split_info[1]  # id값만 가지고 있다.

        # 나간 사람이 다시 안들어올 수도 있다. 즉, result_data에 값이 없을수도 있다.
        if id not in result_data:
            result.append("{}님이 나갔습니다.".format(leave_id[id]))
        else:
            result.append("{}님이 나갔습니다.".format(result_data[id]))

print(result_data)
print(result)

#########################
# 위의 풀이는 이미 한번 배정하고 한번 더 배정하였다.
# 밑의 풀이도 시간복잡도는 비슷하지만 실제 연산량은 더 작아보인다.
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer