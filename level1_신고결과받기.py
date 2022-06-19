# 해당 방법은 딕셔너리를 이용하여 해결하였다.
# 중복되는 값들은 set을 이용하여 삭제하고, 총 id들을 key값으로 가지는 딕셔너리를 2개를 만든다.
# report에 있는 신고 이용자들의 전체 신고 빈도수를 딕셔너리의 value값으로 구한다.
# 이후 신고한 사람의 누적 신고수가 k개 이상이면 신고메세지를 보내므로 report의 첫번째 인자 자리에 신고메세지를 보낸 신고자 수를 저장하도록 한다.

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]


def solution(id_list, report, k):
    # k : k번 신고된 유저는 게시판 이용이 정지된다.
    # report는 이용자id 신고한id 형태의 문장열로 구성된다.
    # 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return하도록 한다.

    uniq = list(set(report))  # 먼저 중복된 값들은 제거한다. -> 똑같은 사람을 신고하면 카운트 x
    reports = [i.split(" ") for i in uniq]

    id = {}
    final_id = {}  # 최종 id별 신고자 수 구하기

    for i in id_list:  # id별 딕셔너리 초기화
        id[i] = 0
        final_id[i] = 0

    # 신고당한 총 개수 구하기
    for i in range(len(reports)):
        person_report = reports[i][1]
        id[person_report] += 1

    answer = [0] * len(id_list)
    for i in range(len(reports)):
        person = reports[i][0]
        person_report = reports[i][1]

        if id[person_report] >= k:
            final_id[person] += 1

    answer = list(final_id.values())
    print(list(final_id.values()))

    return answer

###############
# 또 다른 방법 --> index()를 사용하여 값을 추가하였다.
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer