board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4] # 작동시킨 위치

store = []  # 뽑힌 인형들이 들어가는 바구니
move_index = [i-1 for i in moves]  # 배열 인덱스와 같이 맞추기

# print(board[:][move_index[0]])
count = 0
for col in move_index:
    for row in range(len(board)):
        item = board[row][col]

        if item == 0:
            continue

        if item != 0: # 아이템이 존재

            if len(store) > 0:  # store에 값이 존재하면 두개 비교
                temp = store[-1] # 마지막 원소 비교

                if temp == item:
                    count = count + 2
                    del store[-1]  # 아이템 두개 삭제
                    board[row][col] = 0
                else:
                    store.append(item)
                    board[row][col] = 0
            else:  # store가 비어있을 때 --> 값 넣기
                store.append(item)  # 장바구니에 아이템 추가
                board[row][col] = 0  # 뽑으면 해당 아이템은 사라진다.
            break

print(board)
print(count)

########################
# stack 리스트에 아이템들을 넣고 -1과 -2 인덱스를 서로 비교하여 값들을 제거하는 방법도 있다.
