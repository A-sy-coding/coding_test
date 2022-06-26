# 스코빌 지수가 가장 낮은 두개의 음식을 섞어 새로운 음식을 만든다.
# 새로운 음식 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될때까지 반복한다.

score = [1, 2, 3, 9, 10, 12]
k = 7

# 최대 score 길이 - 1 만큼 반복할 수 있다.
count = 0
for i in range(len(score)-1):
    score.sort() # 오름차순으로 정렬

    if min(score) < k:  # k보다 작으면 섞는다.
        blend = score[0] + (score[1]*2)
        score.pop(0)
        score.pop(0)
        score.append(blend)
        count += 1
if min(score) < k and len(score) == 1 :
    answer = -1
# print(score)
# print(count)

######################
# 위의 코드는 시간 효율성 측면에서 좋지 않다.
# sort를 사용하면 시간초과가 나온다.
# 따라서 heapq를 사용한다. --> heapq는 push,pop을 할때 자동으로 정렬해준다.
import heapq as h
score = [1, 2, 3, 9, 10, 12]
k = 7

heap = []
for i in score:
    h.heappush(heap, i)

count = 0
for i in range(len(heap)-1):
    if heap[0] < k:  # k보다 작으면 섞는다.
        h.heappush(heap, h.heappop(heap) + h.heappop(heap)*2)
        count += 1

if heap[0] < k and len(heap) == 1 :
    count = -1


print(heap)
print(count)