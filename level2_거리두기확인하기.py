# 강의실은 5*5
# P : 응시자가 앉아있는 자리
# O : 빈 테이블
# X : 파티션
# 맨해튼 거리 = abs(r1-r2) + abs(c1-c2)
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

# p가 있는 좌표 구해보기
answer = []
for place in places:
    coord = []
    for x in range(len(place)):
        for y in range(len(place[x])):
            if place[x][y] == 'P':
              coord.append([x,y])

    if len(coord) == 0:
        answer.append(1)
        continue

    flag = 0
    result = 1
    for i in range(len(coord)-1):
        r1,c1 = coord[i]
        for j in range(i+1, len(coord)):
            r2,c2 = coord[j]
            distance = abs(r1-r2) + abs(c1-c2)
            if distance == 1:
                result = 0
                flag = 1
                break
            elif distance == 2:
                min_y = min(c1,c2)
                min_x = min(r1,r2)
                if r1 == r2 and  place[r1][min_y+1] != 'X':  # 같은 행에 존재할 때 중간에 X가 있어야 됨
                    result = 0
                    flag = 1
                    break
                elif c1 == c2 and place[min_x+1][c1] != 'X':
                    result = 0
                    flag = 0
                    break
                elif c1 > c2:  # 무조건 r1이 더 위쪽에 있게 된다.
                    if place[r1][c1-1] != 'X' or place[r2][c2+1] != 'X':
                        result = 0
                        flag = 0
                        break
                elif c1 < c2:
                    if place[r1][c1+1] != 'X' or place[r2][c2-1] != 'X':
                        result = 0
                        flag = 0
                        break

        if flag:
            break
    answer.append(result)

print(answer)
