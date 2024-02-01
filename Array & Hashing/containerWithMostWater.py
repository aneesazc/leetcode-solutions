# Time - O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        res = 0

        while L < R:
            area = (R - L) * min(height[L], height[R])
            res = max(res, area)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return res
