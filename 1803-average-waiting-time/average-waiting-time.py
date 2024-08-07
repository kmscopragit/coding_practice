class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        answer = 0
        end_time = 0
        cnt = 0
        for s, t in customers:
            cnt += 1
            end_time = max(end_time, s) + t
            answer += end_time - s
            # if s >= end_time:
            #     answer += t
            #     end_time = s + t
            # else:
            #     end_time = end_time + t
            #     answer += end_time - s
        return answer/cnt