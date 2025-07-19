class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0]

        # curr_idx = 0
        # while curr_idx < len(cost):
        #     if cost[curr_idx] < cost[curr_idx+1]:
        #         dp.append(dp[-1] + cost[curr_idx])
        #         curr_idx = curr_idx + 2
        #     else:
        #         dp.append(dp[-1] + cost[curr_idx+1])
        #         curr_idx = curr_idx + 1
        
        # return dp[-1]
        cost.append(0)

        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])
