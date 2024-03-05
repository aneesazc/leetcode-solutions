# O(nlogn)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) # -8
            second = heapq.heappop(stones) # -7
            if second > first:
                heapq.heappush(stones, -(second - first))
                # heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])
