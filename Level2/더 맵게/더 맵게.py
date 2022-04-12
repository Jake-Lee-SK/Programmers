import heapq
def solution(scoville, K):
    scoville.sort()
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        a = heapq.heappop(scoville)
        b = 2*heapq.heappop(scoville)
        heapq.heappush(scoville, a+b)
        answer += 1
    return answer

# 시간 내 해결하기 위해서는 heap 필수.