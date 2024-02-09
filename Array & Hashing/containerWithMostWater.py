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



class Solution2:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        res = 0

        while L < R:
            currArea = (R - L) * min(height[L], height[R])
            res = max(res, currArea)
            if height[L] < height[R]:
                L += 1
            elif height[R] <= height[L]:
                R -= 1

        return res

# why R - L and not R - L + 1
# Here, you're not counting the elements but measuring how far apart the two points are. 
# Since the problem models a continuous space where points represent positions along the x-axis, 
# the distance between two points L and R is the difference in their positions.
# In essence, when calculating area in this problem, you're looking at how many units apart the two vertical lines are, 
# not how many vertical lines are between them. T
# he height of the water container is determined by the shorter of the two lines (min(height[L], height[R])), 
# as the water would overflow from the shorter side.

